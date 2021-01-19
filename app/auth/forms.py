from flask_wtf import FlaskForm as Form
from wtforms.fields.core import StringField, BooleanField
from wtforms.fields.simple import SubmitField, PasswordField
from wtforms.validators import Required, Email, EqualTo, DataRequired

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)
	submit = SubmitField('Login')