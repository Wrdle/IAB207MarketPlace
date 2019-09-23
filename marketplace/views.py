from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search')
def search():
    return render_template('search.html')

@bp.route('/log_sign')
def log_sign():
    return render_template('log_sign.html')