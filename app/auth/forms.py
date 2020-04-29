from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Email,DataRequired, EqualTo,ValidationError
from app.auth.models import Users





class RegForm(FlaskForm):

    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("password", validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password',
     message='Passwords must match')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("password", validators = [DataRequired()])
    submit = SubmitField('Login')
