from flask import Blueprint, render_template

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
    return render_template('item.html')

@bp.route('/create')
def createItem():
    return render_template('create_item.html')