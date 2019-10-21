from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from . import db

#create blueprint
bp = Blueprint('auth', __name__)

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    error=None
    if(form.validate_on_submit()):
        user_name = form.username.data
        password = form.password.data
        u1 = User.query.filter_by(username=user_name).first()
        
        # Check if there is user with that name
        if u1 is None:
            error='Incorrect user name'
        #check the password - notice password hash function
        elif not check_password_hash(u1.password_hash, password): # takes the hash and password
            error='Incorrect password'
        if error is None:
        #sign in and set the login user
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            print(error)
            flash(error)
        #it comes here when it is a get method
    return render_template('login.html', pageTitle="Compubay Login", form=form, heading='Login')

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Register form submitted')
        #get username, password and email from the form
        uname = form.username.data
        pwd = form.password.data
        emailaddress = form.email.data
        number = form.phone.data
        # don't store the password - create password hash
        pwd_hash = generate_password_hash(pwd)
        #create a new user model object
        new_user = User(username=uname, password_hash=pwd_hash, email=emailaddress, phone=number)
        db.session.add(new_user)
        db.session.commit()
        #commit to the database and redirect to HTML page
        return redirect(url_for('auth.register'))
    
    return render_template('login.html', pageTitle="Compubay Register", form=form, heading='Register')

@bp.route('/logout')
def logout():
    logout_user()
    return render_template('logout.html', pageTitle="Compubay Logout")