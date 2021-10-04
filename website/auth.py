#Manage templates
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
#Manage user sessions, related to hernece UserMixin
from flask_login import login_user,login_required, logout_user,current_user


auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #Query in the system
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Welcome to our web!', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('User & password are not correct!', category='error')
        else:
            flash(f'the user {email} doesn\'t exist', category='error')
    return render_template("login.html",user=current_user)

@auth.route('/logout')
@login_required #decorator to force only access when is login
def logout():
    data = request.form
    print(data)
    logout_user()
    flash('You were disconected!', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    #return "<p>Sign Up</p>"
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Query in the system
        user = User.query.filter_by(email=email).first()
        if user:
            flash(f'User with {email} already exist', category='error')
        elif len(email)<4:
            #send a message to the front, in the template
            #message and category varaibles
            flash('Email must be greater than 4 chacarters',category='error')
        elif len(name)<2:
            flash('Name must be greater than 2 characters',category='error')
        elif len(password1)<7:
            flash('Name must be greater than 7 characters',category='error')
        elif password1 != password2:
            flash('Name must be greater than 7 characters',category='error')
        else:
            new_user = User(email=email,password=generate_password_hash(password1,method='sha256'),first_name=name)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html",user=current_user)