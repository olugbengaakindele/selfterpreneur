from app.auth import auth
import os
from flask import render_template, url_for, redirect, request, flash
from app.auth.forms import RegForm, LoginForm, DeleteForm
from app.auth.models import Users
from flask_login import login_user, logout_user, login_required
from app import bcrypt,db
from app import Message, mail, SECRET_KEY_2
from itsdangerous import URLSafeTimedSerializer,SignatureExpired,BadTimeSignature
from datetime import datetime

s = URLSafeTimedSerializer('Thisissecret')

@auth.route('/home')
def home():
    return render_template('layout.html', title='home_page')


@auth.route('/register', methods=['GET', 'POST'])
def reg_user():
    form = RegForm()
    name = None
    email = None
    password = None

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        email_con = email
        email_exists = Users.query.filter_by(user_email =  email).first()
        if email_exists:
            flash(u'Email already exist, please login into your account', 'error')
            return redirect(url_for('auth.reg_user'))
        else:
            # the function below creates new user records in database
            Users.create_user(name, email, password)
            flash('Registration Successful, an email confirmation link has been sent to your email', category='success')

            #this part send emil verfication link
            token = s.dumps(email_con, salt = 'email_verify')
            msg = Message('Confirm Email', sender ='akindelegbenga@gmail.com', recipients=[email_con])
            link = url_for('auth.verify_email', token = token, _external= True)
            msg.body = 'Your link is {}'.format(link)
            mail.send(msg)
            return redirect(url_for('me.home'))

    return render_template('reg.html', form=form)



#this url takes in the emil verifiction
@auth.route('/email_verification/<token>')
def verify_email(token):

    try:
        email_con = s.loads(token, salt = 'email_verify',max_age= 3600)

    except SignatureExpired:
        return '<h3>Your token expired</h3>'
    except BadTimeSignature:

        return '<h3>Wrong Link</h3>'

    user = Users.query.filter_by(user_email=email_con).first()
    if user.email_confirmed:
        flash('Account already confirmed. Please login.', 'info')
    else:
        user.email_confirmed = True
        user.email_confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Thank you for confirming your email address!')
    return redirect(url_for('me.home'))

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    user_email = None
    password = None

    if form.validate_on_submit():
        user_email = form.email.data
        password = form.password.data

        # check if email exist
        email_exist = Users.query.filter_by(user_email=user_email).first()
        if email_exist:
            # check if pasword match email
            if bcrypt.check_password_hash(email_exist.user_password, password):

                login_user(email_exist,form.remember_me.data)
                return redirect(url_for('me.myprofile'))
          
   
    return render_template('signin.html', form=form)



@auth.route('/signout')
@login_required
def signout():
           
    logout_user()
    return redirect(url_for('me.home'))


#this routes deletes exisitinfg emails to be used for testing 
@auth.route("/delete")
def delete_email():
    form = DeleteForm()

    return render_template("delete_email.html", form = form )


