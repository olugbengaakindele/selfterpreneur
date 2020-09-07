from app import db
from flask_sqlalchemy import SQLAlchemy
from app import bcrypt
from app import login_manager
from datetime import datetime
from flask_login import login_user, logout_user, login_required

class Personal_Info(db.Model):
    __tablename__ = 'personal_info'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    user_mobile_phone = db.Column(db.String(100))
    user_work_phone = db.Column(db.String(100))
    user_city = db.Column(db.String(100), nullable=False)
    user_province =  db.Column(db.String(100), nullable=False)



    def __init__(self, user_name,user_email, user_mobile_phone, user_work_phone, user_city, user_province):
        self.user_name = user_name
        self.user_email = user_email
        self = user_mobile_phone
        self.user_work_phone = user_work_phone
        self.user_city = user_city
        self.user_province = user_province

    def __repr__(self):
        return ("Personal Info Created")

    @classmethod
    def create_personal_info(cls, name, email,  mobile_phone, user_work_phone, city,province):
        user = cls(user_name=name,
                   user_email= email,
                   user_mobile_phone=mobile_phone,
                   user_work_phone = user_work_phone,
                   user_city=city,
                   user_province = province)

        db.session.add(user)
        db.session.commit()
        return user
