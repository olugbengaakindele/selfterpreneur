from app import db
from flask_sqlalchemy import SQLAlchemy
from app import bcrypt

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100),nullable = False)
    user_email = db.Column(db.String(100),nullable = False)
    user_password = db.Column(db.String(100),nullable = False)

    def __init__(self, user_name, user_email,user_password):
        self.user_name =user_name 
        self.user_email = user_email
        self.user_password= user_password

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
