# app/me/routes

from app.me import me
from flask import render_template, request, redirect, url_for


@me.route("/me/<myemail_id>")
def myprofile(myemail_id):
    return render_template("myprofile.html")


@me.route("/failedlogin")
def failedlogin():
    return "failed_login"


@me.route("/home")
def home():
    return "home.html"

