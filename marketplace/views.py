from flask import Blueprint, render_template, request
from .models import Listing
from sqlalchemy import and_, desc

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    listings = Listing.query.order_by(desc(Listing.post_date)).limit(4).all()
    return render_template('index.html', listings=listings)

@bp.route('/search', methods=['GET','POST'])
def search(): 
    searchKeywords = request.args.get('searchKeywords')
    searchCategory = request.args.get('searchCategory')
    if (searchKeywords != None):     
        listings = Listing.query.filter(and_(Listing.name.like("%" + searchKeywords + "%"), Listing.category == searchCategory)).all()
    else:
        listings = Listing.query.filter(Listing.category == searchCategory).all()
    return render_template('search.html', listings = listings, search=searchKeywords)