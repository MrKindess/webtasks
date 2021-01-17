from flask_wtf import FlaskForm as Form
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import Required, ValidationError, DataRequired, \
    Email, EqualTo, Length

class LoginForm(Form):
    email = StringField(label=('Email'),
                        validators=[DataRequired(),
                                    Email(),
                                    Length(max=120)])
    password = PasswordField(label=('Password'),
                             validators=[DataRequired(),
                                         Length(min=8, message='Password should be at least %(min)d characters long')])
    confirm_password = PasswordField(
        label=('Confirm Password'),
        validators=[DataRequired(message='*Required'),
                    EqualTo('password', message='Both password fields must be equal!')])
