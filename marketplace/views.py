from flask import Blueprint, render_template, request
from .models import Listing
from sqlalchemy import and_

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search', methods=['GET','POST'])
def search(): 
    searchKeywords = request.args.get('searchKeywords')
    searchCategory = request.args.get('searchCategory')
    if (searchKeywords != None):     
        listings = Listing.query.filter(and_(Listing.name.like("%" + searchKeywords + "%"), Listing.category == searchCategory)).all()
    else:
        listings = Listing.query.filter(Listing.category == searchCategory).all()
    return render_template('search.html', listings = listings, search=searchKeywords)

@bp.route('/log_sign')
def log_sign():
    return render_template('log_sign.html')