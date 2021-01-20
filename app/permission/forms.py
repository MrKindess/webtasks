from flask_wtf import FlaskForm as Form
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import Required, ValidationError, DataRequired, \
    Email, EqualTo, Length

class FormPermission(Form):
    name = StringField('Name', validators=[DataRequired()])
    descripton = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
