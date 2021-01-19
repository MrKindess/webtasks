from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.users.forms import UserForm
from app.users.models import User
users = Blueprint('users', __name__, url_prefix='/users')

# Set the route and accepted methods
@users.route('/', methods=['GET'])
def index():
	return render_template('modules/users/index.html')

@users.route('/create', methods=['GET'])
def create():
    form  = UserForm()

    return render_template('modules/users/create.html', form=form)

