from . import db
from datetime import datetime

class User(db.Model):
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
    item_name = db.Column(db.String(50), nullable=False)
    post_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    item_description = db.Column(db.String(400))
    item_suburb = db.Column(db.String(50), nullable=False)
    item_price = db.Column(db.Integer, default=0)
    item_category = db.Column(db.String(15), nullable=False)
    item_cpu = db.Column(db.String(50))
    item_ramgb = db.Column(db.Integer)
    item_totalgb = db.Column(db.Integer)

    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'))



    
