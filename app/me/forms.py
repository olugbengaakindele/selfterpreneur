from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets



def num_validate(form, field):
    check = len(field.data)
    if check != 10:
        raise ValidationError('Number is greater than 10 digits')
    '''elif isinstance(check, int):
        raise ValidationError('Only digits allowed')'''

class FrmPersonalInfo(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    mobile_phone = StringField('Mobile Number', validators=[DataRequired(), num_validate])
    work_phone = StringField('Work Number', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province', validators=[DataRequired()])
    submit = SubmitField('Submit')
