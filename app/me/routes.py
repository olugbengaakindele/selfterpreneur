# app/me/routes

from app.me import me
from flask import render_template, request, redirect, url_for


@me.route("/<myemail_id>")
def myprofile(myemail_id):
    # get the info from  personal, business and socail media to render
    return render_template("myprofile.html")


@me.route("/<myemail_id>/personalinfo")
def personalinfo(myemail_id):
    # get the info from  personal, business and socail media to render
    return render_template("myprofile.html")


@me.route("/home")
def home():
    return "home.html"
