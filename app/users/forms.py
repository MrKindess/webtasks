from flask_wtf import FlaskForm as Form
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import Required, ValidationError, DataRequired, \
    Email, EqualTo, Length, InputRequired

class CreateUserForm(Form):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    email = StringField('Email', validators=[DataRequired(message="Email is required!"), Email()])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required!")])
    phone = StringField('Phone')
    submit = SubmitField('Save')

class EditUserForm(Form):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    email = StringField('Email', validators=[DataRequired(message="Email is required!"), Email()])
    password = PasswordField('Password')
    phone = StringField('Phone')
    submit = SubmitField('Save')
