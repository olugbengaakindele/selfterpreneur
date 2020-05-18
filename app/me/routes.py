# app/me/routes

from app.me import me
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.me.forms import FrmPersonalInfo
from app.me.models import  Personal_Info



@me.route("/<myemail_id>")
@login_required
def myprofile(myemail_id):
    # get the info from  personal, business and socail media to render
    return render_template("mypage.html")


@me.route("/<myemail_id>/personalinfo")
@login_required
def personalinfo(myemail_id):
    form = FrmPersonalInfo()
    if form.validate_on_submit():
        return redirect(url_for('me.personalinfo'))


    # get the info from  personal, business and socail media to render
    return render_template("personalinfo.html", form = form )


@me.route("/home")
def home():
    return "home.html"