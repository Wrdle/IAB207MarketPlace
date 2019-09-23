from flask import Blueprint, render_template
from .models import User, Listing
from . import db


bp = Blueprint('item', __name__, url_prefix='/item')

@bp.route('/<id>/update')
def updateItem(id):
    # Will use id to know which computer the user wants to update the listing on.
    # Will query the db for the information and display it in the corrosponding boxes for editing
    return render_template('update_item.html')

@bp.route('/<id>/bids')
def bids(id):
    # Will use id to know which computer the user wants to update the listing on.
    # Will query the db for the information and display it in the corrosponding boxes for editing
    return render_template('bids.html')

@bp.route('/<id>')
def item(id):
    # Will use id to get computer information. Will query DB for this
    listing = Listing.query.filter_by(id=id).first()
    sellerid = Listing.seller_id
    return render_template('item.html', listing=listing, seller=User.query.filter_by(id=sellerid).first())

@bp.route('/create')
def createItem():

    usera = User(username = 'johnnyjon', email = 'john@gmail.com', password_hash = '44a44', phone='0400000000')
    db.session.add(usera)
    
    listing = Listing(user=usera, item_name='Xtreme Gamor PC', item_description = 'Get XTREME cooling PC', item_category='PC', item_suburb = 'Wakerley', item_price=50.05, item_cpu='Intel i10', item_ramgb=2, item_totalgb=256)
    db.session.add(listing)
    db.session.commit()

    return render_template('create_item.html')

def get_listing():
    listingResult = Listing.query.filter_by(id=id).first()
    return listingResult