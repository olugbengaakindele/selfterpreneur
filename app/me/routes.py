# app/me/routes

from app.me import me
from app.auth.models import Users
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required
from app.me.forms import frmProfile, frmTest
from app.me.models import Personal_Info
from app import db


@me.route("/myaccount/profilesummary",methods=["GET","POST"])
@login_required
def myprofile():
    form =  frmTest()
   
    if form.validate_on_submit():
        #check if user exist 
        user_info = Personal_Info.query.filter_by(user_email=form.email.data).first()
        if user_info:
            #Edit profile data
            user_info.user_name = form.name.data
            user_info.user_email = form.email.data
            user_info.user_mobile_phone = form.mobile_phone.data
            user_info.user_work_phone = form.work_phone.data
            user_info.user_city = form.city.data
            user_info.user_country = form.country.data
            db.session.add(user_info)
            db.session.commit()
            flash("Personal Info has been updated")
            return redirect(url_for('me.myprofile'))
        else:

            name = form.name.data
            email = form.email.data
            mobile_phone = form.mobile_phone.data
            work_phone = form.work_phone.data
            city = form.city.data
            country = form.country.data
            postcode = form.postcode.data
            # load to database
            Personal_Info.create_personal_info(
                name, email, mobile_phone, work_phone,postcode, city, country,"","","","")
           
            flash('form was validated')
            return render_template("mypage.html", form = form)


    return render_template("mypage.html", form = form)


@me.route("/personalinfo", methods=['GET', 'POST'])
@login_required
def personalinfo():
    form = frmProfile()
    name = None
    email = None
    mobile_phone = None
    work_phone = None
    city = None
    province = None

    if form.validate_on_submit():
        user_info = Personal_Info.query.filter_by(user_email= myemail_id).first()
        # if user already has personal info details then update record else create new one
        if user_info:
            user_info.user_name = form.name.data
            user_info.user_email = form.email.data
            user_info.user_mobile_phone = form.mobile_phone.data
            user_info.user_work_phone = form.work_phone.data
            user_info.user_city = form.city.data
            user_info.user_province = form.province.data
            db.session.add(user_info)
            db.session.commit()
            flash("Personal Info has been updated")
            return redirect(url_for('me.myprofile', myemail_id = myemail_id))

        else:
            name = form.name.data
            email = form.email.data
            mobile_phone = form.mobile_phone.data
            work_phone = form.work_phone.data
            city = form.city.data
            province = form.province.data
            # load to database
            Personal_Info.create_personal_info(
                name, email, mobile_phone, work_phone, city, province)
            return redirect(url_for('me.myprofile', myemail_id=email))

    # get the info from  personal, business and socail media to render
    return render_template("personalinfo.html", form=form)


@me.route("/profilesetting", methods=["GET", "POST"])
def profilesetting():
    
    form_Profile = frmProfile()
    user_exist= Personal_Info.query.filter_by(user_email = form_Profile.email.data).first()

    if form_Profile.validate_on_submit():
        #check if user already exist
        if user_exist:
            Personal_Info.user_email = form_Profile.email.data
            db.session.add(user_exist)
            db.session.commit()
            return redirect(url_for("auth.home"))
        else:
           
            return redirect(url_for("auth.signin"))

    return render_template("profilesetting.html", form=form_Profile)

@me.route("/account/account",methods=["GET","POST"])
@login_required
def myaccount():

    return render_template("myaccount.html")