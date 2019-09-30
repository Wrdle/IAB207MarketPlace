from flask import Blueprint, render_template, request
from .models import Listing
from sqlalchemy import and_

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/search', methods=['GET','POST'])
def search(): 
    search = request.args.get('searchKeywords')
    searchCategory = request.args.get('searchCategory')
    listings = Listing.query.filter(and_(Listing.name.like("%" + search + "%"), Listing.category == searchCategory)).all()
    return render_template('search.html', listings = listings, search=search)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')