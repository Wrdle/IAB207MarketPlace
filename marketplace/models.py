from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    phone = db.Column(db.String(50))

    listings = db.relationship('Listing', backref='user')

class Listing(db.Model):
    __tablename__='listings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    post_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    description = db.Column(db.String(400))
    suburb = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, default=0)
    category = db.Column(db.String(15), nullable=False)
    cpu = db.Column(db.String(50))
    ramgb = db.Column(db.Integer)
    totalgb = db.Column(db.Integer)
    image = db.Column(db.String(200), nullable=False)

    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))



    
