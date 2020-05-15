from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from app.auth.models import Users
from app import bcrypt

class FrmPersonalInfo(FlaskForm):
    
    name = StringField("Name", validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired()])
    mobile_phone= StringField('Mobile Number', validators=[DataRequired()])
    work_phone= StringField('Work Number', validators=[DataRequired()])
    city= StringField('City', validators=[DataRequired()])
    province= StringField('Province', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')