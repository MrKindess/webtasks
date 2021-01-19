from flask_wtf import FlaskForm as Form
from wtforms import TextField, PasswordField # BooleanField
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import Required, Email, EqualTo, DataRequired
from flask_wtf import FlaskForm

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')