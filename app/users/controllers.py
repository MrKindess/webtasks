# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug.security import generate_password_hash, check_password_hash

# Import the database object from the main app module
from app import db

# Import module forms
from app.users.forms import LoginForm

# Import module models (i.e. User)
from app.users.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
users = Blueprint('users', __name__, url_prefix='/users')

# Set the route and accepted methods
@users.route('/', methods=['GET'])
def index():
	return render_template('modules/users/index.html')

@users.route('/create', methods=['GET'])
def create():
    return render_template('modules/users/create.html')

