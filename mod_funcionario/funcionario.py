from flask import Blueprint, render_template, request, redirect, url_for
from mod_funcoes.funcoes import Funcoes
import requests

bp_funcionario = Blueprint(
    'funcionario', __name__, url_prefix="/funcionario", template_folder='templates')


''' endereços do endpoint, dentro de variáveis '''
urlApiFuncionarios = "http://localhost:8000/funcionario/"
urlApiFuncionario = "http://localhost:8000/funcionario/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas utilizando as variáveis '''
@bp_funcionario.route('/', methods=['GET', 'POST'])
def formListaFuncionario():
    try:
        response = requests.get(urlApiFuncionarios, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaFuncionario.html', result=result)
    except Exception as e:
        return render_template('formListaFuncionario.html', erro=e)

@bp_funcionario.route('/form-funcionario/', methods=['POST'])
def formFuncionario():
    return render_template('formFuncionario.html')

@bp_funcionario.route('/insert', methods=['GET','POST'])
def insert():
    try:

        id_funcionario = 0
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])

        payload = {'id_funcionario': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': cpf, 'telefone': telefone, 'grupo': grupo, 'senha': senha}

        response = requests.post(urlApiFuncionarios, headers=headers, json=payload)
        result = response.json()
        return redirect( url_for('funcionario.formListaFuncionario', msg=result) )
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e)
    
@bp_funcionario.route("/form-edit-funcionario", methods=['POST'])
def formEditFuncionario():
    try:

        id_funcionario = request.form['id']

        response = requests.get(urlApiFuncionarios + id_funcionario, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])

        return render_template('formFuncionario.html', result=result[0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])
    
@bp_funcionario.route('/edit', methods=['POST'])
def edit():
    try:

        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])

        payload = {'id_funcionario': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': cpf, 'telefone':

        telefone, 'grupo': grupo, 'senha': senha}

        response = requests.put(urlApiFuncionarios + id_funcionario, headers=headers, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect( url_for('funcionario.formListaFuncionario', msg=result[0]) )
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])
    
@bp_funcionario.route('/delete', methods=['POST'])
def delete():
    try:

        id_funcionario = request.form['id_funcionario']

        response = requests.delete(urlApiFuncionarios + id_funcionario, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect(url_for('funcionario.formListaFuncionario', msg=result[0]))

    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])