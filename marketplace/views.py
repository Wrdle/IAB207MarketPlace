from flask import Blueprint, render_template, request
from .models import Listing

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search', methods=['GET','POST'])
def search():
    search = request.args.get('searchKeywords')
    listings = Listing.query.filter(Listing.item_name.like("%" + search + "%")).all()
    return render_template('search.html', listings = listings, search=search)

@bp.route('/log_sign')
def log_sign():
    return render_template('log_sign.html')