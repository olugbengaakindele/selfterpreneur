from app.auth import auth
from flask import render_template, url_for, redirect, request, flash
from app.auth.forms import RegForm, LoginForm
from app.auth.models import Users
from flask_login import login_user, logout_user, login_required
from app import bcrypt


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

        email_exists = Users.query.filter_by(user_email =  email).first()
        if email_exists:
            flash(u'Email already exist, please login into your account', 'error')
            return redirect(url_for('auth.reg_user'))
        else:
            # the function below creates new user records in database
            Users.create_user(name, email, password)
            flash('Registration Successful', category='success')
            return redirect(url_for('me.home'))

    return render_template('reg.html', form=form)


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
