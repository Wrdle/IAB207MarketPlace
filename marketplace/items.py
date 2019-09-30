from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug import secure_filename
import uuid
import os
from .models import User, Listing
from .forms import CreateItemForm
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
    if (listing != None): 
        return render_template('item.html', listing=listing, seller=User.query.filter_by(id=sellerid).first())
    return render_template('404.html')

@bp.route('/create', methods = ['GET', 'POST'])
def createItem():
    form = CreateItemForm()

    if form.validate_on_submit():
        usera = User(username = 'johnnyjon', email = 'john@gmail.com', password_hash = '44a44', phone='0400000000')
        db.session.add(usera)

        fp = form.image.data
        filename = fp.filename
        filename, ext = os.path.splitext(filename)
        filename = uuid.uuid4().hex + ext
        # get the current path of the module file… store file relative to this path
        BASE_PATH = os.path.dirname(__file__)
        #upload file location – directory of this file/static/image
        upload_path = os.path.join(BASE_PATH, 'static/img/listings', secure_filename(filename))
        # store relative path in DB as image location in HTML is relative
        db_upload_path = '/static/img/listings/'+ secure_filename(filename)
        # save the file and return the db upload path
        fp.save(upload_path)

        newListing = Listing(user= usera, name=form.name.data, description=form.description.data,
        suburb=form.suburb.data, state=form.state.data, price=form.price.data,
        category=form.category.data, cpu= form.cpu.data, ramgb=form.ramgb.data, 
        totalgb=form.totalgb.data, image=filename)

        db.session.add(newListing)
        db.session.commit()
        return redirect(url_for('item.createItem'))
    return render_template('create_item.html', form=form)

def get_listing():
    listingResult = Listing.query.filter_by(id=id).first()
    return listingResult