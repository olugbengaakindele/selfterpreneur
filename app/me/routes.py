#app/me/routes

from app.me import me


@me.route("/myprofile")
def myprofile():


    return "me"