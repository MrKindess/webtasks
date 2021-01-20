from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from app import db
from app.roles.models import Role
from app.roles.models import UserRole
from app.roles.models import UserRole

roles = Blueprint('roles', __name__, url_prefix='/roles')


# Set the route and accepted methods
@roles.route('/', methods=['GET'])
def index():
    return render_template('modules/users/index.html')
