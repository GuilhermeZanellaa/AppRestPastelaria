from flask import Blueprint, render_template
bp_index = Blueprint(
    'index', __name__, url_prefix="/index", template_folder='templates')


@bp_index.route('/')
def formListaFuncionario():

    return render_template('formIndex.html'), 200
