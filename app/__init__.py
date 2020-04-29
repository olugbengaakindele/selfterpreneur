from flask import Flask, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt 



db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt = Bcrypt()



def create_app(config_type): #test/dev/ prod
    
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config' , config_type + '.py')
    app.config.from_pyfile(configuration)

    #initialize database to flask app
    db.init_app(app)

    #initialize bootstrap
    bootstrap.init_app(app)
    bcrypt.init_app(app)


    #register blueprit
    from app.auth import auth 
    app.register_blueprint(auth)

    from app.me import me 
    app.register_blueprint(me)


    return app


