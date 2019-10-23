from flask import Blueprint, render_template, request, url_for
from .models import Listing, Sold, User, Bid
from sqlalchemy import and_, desc
from flask_login import login_required, current_user
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    listings = Listing.query.filter(Listing.sold_id == None).all()
    return render_template('index.html', pageTitle="Compubay - Home", listings=listings)

@bp.route('/listings')
@login_required
def listings():
    listings = Listing.query.filter(and_(Listing.seller_id == current_user.id, Listing.sold_id == None)).all()
    return render_template('listings.html', pageTitle="Compubay - Current Listings", listings = listings, current_user=current_user)


@bp.route('/search', methods=['GET','POST'])
def search(): 
    searchKeywords = request.args.get('searchKeywords')
    searchCategory = request.args.get('searchCategory')
    if (searchKeywords != None):     
        listings = Listing.query.filter(and_(Listing.name.like("%" + searchKeywords + "%"), Listing.category == searchCategory,  Listing.sold_id == None)).all()
    else:
        listings = Listing.query.filter(Listing.category == searchCategory, Listing.sold_id == None).all()
    return render_template('search.html', pageTitle="Compubay - Compubay Search", listings = listings, search=searchKeywords)

@bp.route('/past_listings')
@login_required
def past_listings():
    return render_template('past_listing.html', pageTitle="Compubay - Past Listings", db=db)