# app/me/routes

from app.me import me
from app.auth.models import Users
from flask import render_template, request, redirect, url_for,flash,jsonify
from flask_login import login_user, logout_user, login_required
from app.me.forms import frmProfile
from app.me.models import Personal_Info
from app import db


@me.route("/profilesummary/<myemail_id>")
@login_required
def myprofile(myemail_id):
    user = Personal_Info.query.filter_by(user_email = myemail_id).first()
    if user:
        '''user_details = {}
        user_details = { 'name' : user.user_name ,'email' : user.user_email,'m_phone' : user.user_mobile_phone,
                             'w_phone' : user.user_work_phone,'city' : user.user_city,
                             'province' : user.user_province}
        jsonify(user_details)'''
        # get the info from  personal, business and social media to render
        return render_template("mypage.html", user = user)
    else:
        flash("Create a profile")
        return render_template("mypage.html")


@me.route("/personalinfo/<myemail_id>", methods=['GET', 'POST'])
@login_required
def personalinfo(myemail_id):
    form = frmProfile()
    name = None
    email = None
    mobile_phone = None
    work_phone = None
    city = None
    province = None



    if form.validate_on_submit():
        user_info = Personal_Info.query.filter_by(user_email=myemail_id).first()
        #if user already has personal info details then update record else create new one
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
            return redirect(url_for('me.myprofile', myemail_id=myemail_id))
        
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
            return redirect(url_for('me.myprofile',  myemail_id = email))

    # get the info from  personal, business and socail media to render
    return render_template("personalinfo.html", form=form)

@me.route("/profilesetting")
def profilesetting():
    form = frmProfile()
    return render_template("profilesetting.html", form = form)





@me.route("/home")
def home():
    return "index.html"
