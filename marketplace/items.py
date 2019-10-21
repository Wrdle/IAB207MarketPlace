from flask import Blueprint, render_template, redirect, url_for, request, flash, get_flashed_messages
from werkzeug import secure_filename
import uuid
from datetime import datetime
import os
from sqlalchemy import and_, desc
from .models import User, Listing, Bid, Sold
from .forms import CreateItemForm
from . import db
from flask_login import login_required, current_user


bp = Blueprint('item', __name__, url_prefix='/item')

@bp.route('/<id>/bids', methods = ['GET', 'POST'])
@login_required
def bids(id):
    # Will use id to know which computer the user wants to update the listing on.
    # Will query the db for the information and display it in the corrosponding boxes for editing
    listing = Listing.query.filter(and_(Listing.id == id, Listing.sold_id == None)).first()
    if (listing != None):
        bids = Bid.query.filter_by(listing=listing).all()
        
        if (request.method == 'POST'):
            if (request.form.get("buyer")== None):
                flash("You must select a buyer to mark the item as sold.", category="danger")
            elif (request.form.get("price") == None):
                flash("You must enter a price to mark the item as sold.", category="danger")
            elif (request.form.get("sale_date") == ""):
                flash("You must enter the date the item was sold to mark the item as sold.", category="danger")
            else:
                newSale = Sold(listing=listing, sale_price=int(request.form.get("price")),
                 user=User.query.filter_by(id=(request.form.get("buyer"))).first(), 
                 date=datetime.strptime(request.form.get("sale_date"), '%Y-%m-%d'))
                db.session.add(newSale)
                db.session.commit()
                return redirect(url_for('main.listings'))

        if (listing.seller_id == current_user.id):
            return render_template('bids.html', pageTitle=listing.name + "bids", listing = listing, bids=bids)
    return render_template('404.html', pageTitle="404 Error")

@bp.route('/<id>', methods = ['GET', 'POST'])
def item(id):
    # Get the listing
    listing = Listing.query.filter_by(id=id).first()

    # Check if they have pessed the "Placed Expression" Butotn
    if (request.method == 'POST'):
        if (current_user.is_authenticated == False):
            flash("You must login first to place an expression of interest.", category="danger")
        else:
            if (Bid.query.filter(and_(Bid.item_id == listing.id, Bid.bidder_id == current_user.id)).all()):
                flash("You have already placed an expression on this item.", category="danger")
            else:
                db.session.add(Bid(listing=listing, user=current_user))
                db.session.commit()
                flash("You have successfully placed an expression on this item", category="success")

    if (listing != None): 
        sellerid = listing.seller_id
        return render_template('item.html', pageTitle=listing.name, listing=listing, seller=User.query.filter_by(id=sellerid).first(), current_user=current_user)
    return render_template('404.html', pageTitle="404 Error")

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def createItem():
    form = CreateItemForm()

    if form.validate_on_submit():

        fp = form.image.data
        filename = fp.filename
        filename, ext = os.path.splitext(filename)
        filename = uuid.uuid4().hex + ext
        # get the current path of the module file… store file relative to this path
        BASE_PATH = os.path.dirname(__file__)
        #upload file location – directory of this file/static/image
        upload_path = os.path.join(BASE_PATH, 'static/img/listings', secure_filename(filename))
        # save the file and return the db upload path
        fp.save(upload_path)

        newListing = Listing(user= current_user, name=form.name.data, description=form.description.data,
        suburb=form.suburb.data, state=form.state.data, price=form.price.data,
        category=form.category.data, cpu= form.cpu.data, ramgb=form.ramgb.data, 
        totalgb=form.totalgb.data, image=filename)
        db.session.add(newListing)
        db.session.commit()

        return redirect(url_for('item.createItem'))
    return render_template('create_item.html', pageTitle="Create an item",  form=form, current_user=current_user)

def get_listing():
    listingResult = Listing.query.filter_by(id=id).first()
    return listingResult

@bp.route('/<id>/edit', methods = ['GET', 'POST'])
@login_required
def edit_item(id):
    listing = Listing.query.filter_by(id=id).first()
    if (current_user.id == listing.seller_id): 
        form = CreateItemForm(obj=listing)
        if form.validate_on_submit():
            listing.name = form.name.data
            listing.description = form.description.data
            listing.suburb = form.suburb.data
            listing.state = form.state.data
            listing.price = form.price.data
            listing.category = form.category.data
            listing.cpu = form.cpu.data
            listing.ramgb = form.ramgb.data
            listing.totalgb = form.totalgb.data

            fp = form.image.data
            filename = fp.filename
            filename, ext = os.path.splitext(filename)
            filename = uuid.uuid4().hex + ext

            # get the current path of the module file… store file relative to this path
            BASE_PATH = os.path.dirname(__file__)
            #upload file location – directory of this file/static/image
            upload_path = os.path.join(BASE_PATH, 'static/img/listings', secure_filename(filename))
            # save the file and return the db upload path
            fp.save(upload_path)

            listing.image = filename

            db.session.commit()
            flash("You have successfully updated your listing", category="success")
            return redirect(url_for('main.index'))

        return render_template('update_item.html', pageTitle="Edit " + listing.name, form=form, current_user=current_user)
    return render_template('404.html', pageTitle="404 Error")
