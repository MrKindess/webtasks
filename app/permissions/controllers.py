# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.permissions.forms import LoginForm
from app.permissions.models import Permission
permissions = Blueprint('permissions', __name__, url_prefix='/permissions')

@permissions.route('/', methods=['GET'])
def index():
	return render_template('modules/permissions/index.html')

@permissions.route('/create', methods=['GET', ['POST']])
def create():
    return render_template('modules/permissions/create.html')

