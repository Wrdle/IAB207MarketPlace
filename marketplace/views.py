from flask import Blueprint, render_template, request, url_for
from .models import Listing
from sqlalchemy import and_, desc
from flask_login import login_required, current_user

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    listings = Listing.query.order_by(desc(Listing.post_date)).limit(4).all()
    return render_template('index.html', listings=listings)

@bp.route('/listings')
@login_required
def listings():
    listings = Listing.query.filter(Listing.seller_id == current_user.id).all()
    return render_template('listings.html', listings = listings, current_user=current_user)


@bp.route('/search', methods=['GET','POST'])
def search(): 
    searchKeywords = request.args.get('searchKeywords')
    searchCategory = request.args.get('searchCategory')
    if (searchKeywords != None):     
        listings = Listing.query.filter(and_(Listing.name.like("%" + searchKeywords + "%"), Listing.category == searchCategory)).all()
    else:
        listings = Listing.query.filter(Listing.category == searchCategory).all()
    return render_template('search.html', listings = listings, search=searchKeywords)

@bp.route('/past_listing')
@login_required
def pastlisting():
    return render_template('past_listing.html')