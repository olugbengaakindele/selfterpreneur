from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, TextField, TextAreaField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets


def num_validate(form, field):
    check = len(field.data)
    if check != 10:
        raise ValidationError('Number is greater than 10 digits')
    '''elif isinstance(check, int):
        raise ValidationError('Only digits allowed')'''


class frmProfile(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    mobile_phone = StringField('Mobile Number', validators=[DataRequired()])
    work_phone = StringField('Work Number', validators=[DataRequired()])
    country = SelectField('Country', choices=[('1', 'Canada'), ('2', 'UK'), ('3', 'USA')])
    postcode = StringField('Postcode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province', validators=[DataRequired()])
    bio = TextAreaField('Bio')
    submit = SubmitField('Update')

class frmTest(FlaskForm):
    name=StringField('Name')
    email=StringField("Email",validators=[DataRequired(), Email()])
    mobile_phone = StringField('Mobile Number')
    work_phone = StringField('Work Number')
    country = SelectField('Country', choices=[('1', 'Canada'), ('2', 'UK'), ('3', 'USA')])
    postcode = StringField('Postcode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province')
    bio = TextAreaField('Bio')
   
   
    submit= SubmitField("Save")