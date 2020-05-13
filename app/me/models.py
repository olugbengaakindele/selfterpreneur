from app import db
from flask_sqlalchemy import SQLAlchemy
from app import bcrypt
from app import login_manager
from datetime import datetime


class Personal_Info(db.Model):
    __tablename__ = 'personal_info'

    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100),nullable = False)
    user_phone = db.Column(db.String(100))
    user_city = db.Column(db.String(100),nullable = False)
    user_country = db.Column(db.String(100),nullable = False)

    def __init__(self, user_name, user_phone,user_city,user_country):
        self.user_name =user_name
        self.user_phone = user_phone
        self.user_city= user_city
        self.user_country = user_country


    def __repr__(self):
        return ("Account Created")

    @classmethod
    def create_user(cls, name, email, password):
        user = cls(user_name = name,
        user_email= email,
        user_password = bcrypt.generate_password_hash(password).decode('utf-8'))

        db.session.add(user)
        db.session.commit()
        return user
