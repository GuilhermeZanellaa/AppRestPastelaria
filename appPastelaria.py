from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route('/')
def formIndex():
    return "<h1>Rota da página inicial da nossa WEB APP</h1>", 200


@app.route('/funcionario/')
def formListaFuncionario():
    return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200


@app.route('/cliente/')
def formListaCliente():
    return "<h1>Rota da página de Clientes da nossa WEB APP</h1>", 200


@app.route('/produto/')
def formListaProduto():
    return "<h1>Rota da página de Produtos da nossa WEB APP</h1>", 200
