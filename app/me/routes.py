# app/me/routes

from app.me import me
from flask import render_template, request, redirect, url_for,flash
from flask_login import login_user, logout_user, login_required
from app.me.forms import FrmPersonalInfo
from app.me.models import Personal_Info


@me.route("/profilesummary/<myemail_id>")
@login_required
def myprofile(myemail_id):
    # get the info from  personal, business and socail media to render
    return render_template("mypage.html")


@me.route("/personalinfo/<myemail_id>", methods=['GET', 'POST'])
@login_required
def personalinfo(myemail_id):
    form = FrmPersonalInfo()
    name = None
    email = None
    mobile_phone = None
    work_phone = None
    city = None
    province = None

    if form.validate_on_submit():
            name = form.name.data
            email= form.email.data
            mobile_phone = form.mobile_phone.data
            work_phone = form.work_phone.data
            city = form.city.data
            province= form.province.data
            # load to database
            Personal_Info.create_personal_info(
                name,email, mobile_phone, work_phone, city, province)
    
            return redirect(url_for('me.myprofile',  myemail_id = email))

    # get the info from  personal, business and socail media to render
    return render_template("personalinfo.html", form=form)


@me.route("/home")
def home():
    return "home.html"
