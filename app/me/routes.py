#app/me/routes

from app.me import me


@me.route("/myprofile")
def myprofile():


    return "me"

@me.route("/failedlogin")
def failedlogin():

    return "failed_login"

@me.route("/home")
def home():

    return "Registration Succesful"