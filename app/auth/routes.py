from app.auth import auth
from flask import render_template, url_for, redirect, request,flash
from app.auth.forms import RegForm
from app.auth.models import Users


@auth.route('/home')
def home():
    return render_template('layout.html', title='home_page')


@auth.route('/register', methods =['GET', 'POST'])
def reg_user():
    form = RegForm()
    name = None
    email= None
    password= None

    if form.validate_on_submit():
        name =form.name.data
        email = form.email.data
        password = form.password.data

        email_exists = Users.query.filter_by(user_email =  email).first()
        if email_exists:
            flash(u'Email already exist, please login into your account', 'error')
            return redirect(url_for('auth.reg_user'))
        else:
            #the function below creates new user records in database
            Users.create_user(name,email,password)
            flash('Registration Successful', category ='success')
            return redirect(url_for('auth.signin'))
    


    return render_template('reg.html', form=form)



@auth.route('/signin', methods =['GET', 'POST'])
def signin():

    return render_template('signin.html')