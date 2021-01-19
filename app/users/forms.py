from flask_wtf import FlaskForm as Form
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import Required, ValidationError, DataRequired, \
    Email, EqualTo, Length, InputRequired

class UserForm(Form):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    email = StringField('Email', validators=[InputRequired(message="Email is required!"), Email()])
    password = PasswordField('Password', validators=[InputRequired(message="Password is required!")])
    submit = SubmitField('Save')
