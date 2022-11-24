from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import requests
from mod_funcoes.funcoes import Funcoes


bp_cliente = Blueprint('cliente', __name__,
                       url_prefix="/cliente", template_folder='templates')

''' endereços do endpoint '''
urlApiClientes = "http://localhost:8000/cliente/"
urlApiCliente = "http://localhost:8000/cliente/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas dos formulários '''


@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    try:
        response = requests.get(urlApiClientes, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaCliente.html', result=result)
    except Exception as e:
        return render_template('formListaCliente.html', erro=e)


@bp_cliente.route('/form-cliente', methods=['GET', 'POST'])
def formCliente():
    return render_template('formCliente.html'), 200


@bp_cliente.route('/insert', methods=['GET', 'POST'])
def insert():
    try:

        id_cliente = 0
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        dia_fiado = 5
        compra_fiado = True
        senha = Funcoes.cifraSenha(request.form['senha'])

        payload = {'id_cliente': id_cliente, 'nome': nome, 'cpf': cpf, 'telefone': telefone,
                   'dia_fiado': dia_fiado, 'senha': senha, 'compra_fiado': compra_fiado}

        response = requests.post(urlApiClientes, headers=headers, json=payload)
        result = response.json()
        return redirect(url_for('cliente.formListaCliente', msg=result))
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e)


@bp_cliente.route("/form-edit-cliente", methods=['POST'])
def formEditCliente():
    try:

        id_cliente = request.form['id']

        response = requests.get(urlApiClientes + id_cliente, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])

        return render_template('formCliente.html', result=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])


@bp_cliente.route('/edit', methods=['POST'])
def edit():
    try:

        id_cliente = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        dia_fiado = 5
        compra_fiado = True
        senha = Funcoes.cifraSenha(request.form['senha'])

        payload = {'id_cliente': id_cliente, 'nome': nome, 'cpf': cpf, 'telefone': telefone,
                   'dia_fiado': dia_fiado, 'senha': senha, 'compra_fiado': compra_fiado}

        response = requests.put(
            urlApiClientes + id_cliente, headers=headers, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect(url_for('cliente.formListaCliente', msg=result[0]))
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])


@bp_cliente.route('/delete', methods=['POST'])
def delete():
    try:

        id_cliente = request.form['id_cliente']

        response = requests.delete(
            urlApiClientes + id_cliente, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect(url_for('cliente.formListaCliente', msg=result[0]))

    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])
