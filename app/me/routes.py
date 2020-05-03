#app/me/routes

from app.me import me
from flask import render_template , request, redirect, url_for


@me.route("/myprofile")
def myprofile():


    return render_template("home.html")

@me.route("/failedlogin")
def failedlogin():

    return "failed_login"

@me.route("/home")
def home():

    return "home.html"