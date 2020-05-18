from app import db
from flask_sqlalchemy import SQLAlchemy
from app import bcrypt
from app import login_manager
from datetime import datetime


class Personal_Info(db.Model):
    __tablename__ = 'personal_info'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_mobile_phone = db.Column(db.String(100))
    user_work_phone = db.Column(db.String(100))
    user_city = db.Column(db.String(100), nullable=False)
    user_province =  db.Column(db.String(100), nullable=False)
    user_country = db.Column(db.String(100), nullable=False)

    def __init__(self, user_name, user_mobile_phone, user_work_phone, user_city, user_country):
        self.user_name = user_name
        self.user_mobile_phone = user_mobile_phone
        self.user_work_phone = user_work_phone
        self.user_city = user_city
        self.user_country = user_country

    def __repr__(self):
        return ("Personal Info Created")

    @classmethod
    def create_personal_info(cls, name, mobile_phone, work_phone, city, country):
        user = cls(user_name=name,
                   user_mobile_phone=mobile_phone,
                   user_work_phone=work_phone, user_city=city,user_country=country)

        db.session.add(user)
        db.session.commit()
        return user
