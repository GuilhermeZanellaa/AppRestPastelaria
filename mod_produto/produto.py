from flask import Blueprint, render_template, request, redirect, url_for
import requests
from mod_funcoes.funcoes import Funcoes


bp_produto = Blueprint('produto', __name__,
                       url_prefix="/produto", template_folder='templates')

''' endereços do endpoint '''
urlApiProdutos = "http://localhost:8000/produto/"
urlApiProduto = "http://localhost:8000/produto/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}


''' rotas dos formulários '''


@bp_produto.route('/', methods=['GET', 'POST'])
def formListaProduto():
    try:
        response = requests.get(urlApiProdutos, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaProduto.html', result=result)
    except Exception as e:
        return render_template('formListaProduto.html', erro=e)


@bp_produto.route('/form-produto', methods=['GET', 'POST'])
def formProduto():
    return render_template('formProduto.html'), 200


@bp_produto.route('/insert', methods=['GET', 'POST'])
def insert():
    try:

        id_produto = 0
        nome = request.form['nome']
        valor_unitario = request.form['valor']
        descricao = request.form['descricao']
        foto = request.form['foto']

        payload = {'id_produto': id_produto, 'nome': nome,
                   'valor_unitario': valor_unitario, 'descricao': descricao}

        response = requests.post(urlApiProdutos, headers=headers, json=payload)
        result = response.json()
        return redirect(url_for('produto.formListaProduto', msg=result))
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e)


@bp_produto.route("/form-edit-produto", methods=['POST'])
def formEditProduto():
    try:

        id_produto = request.form['id']

        response = requests.get(urlApiProdutos + id_produto, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])

        return render_template('formProduto.html', result=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])


@bp_produto.route('/edit', methods=['POST'])
def edit():
    try:

        id_produto = request.form['id']
        nome = request.form['nome']
        valor_unitario = request.form['valor']
        descricao = request.form['descricao']
        foto = request.form['foto']

        print(id_produto)

        payload = {'id_produto': id_produto, 'nome': nome,
                   'valor_unitario': valor_unitario, 'descricao': descricao}

        response = requests.put(
            urlApiProdutos + id_produto, headers=headers, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect(url_for('produto.formListaProduto', msg=result[0]))
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])


@bp_produto.route('/delete', methods=['POST'])
def delete():
    try:

        id_produto = request.form['id_produto']

        response = requests.delete(
            urlApiProdutos + id_produto, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect(url_for('produto.formListaProduto', msg=result[0]))

    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])
