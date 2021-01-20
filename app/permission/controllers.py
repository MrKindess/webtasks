from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.permission.forms import FormPermission
from app.permission.models import Permission

permission = Blueprint('permissions', __name__, url_prefix='/permissions')

@permission.route('/', methods=['GET'])
def index():
    permissions = Permission.query.all()
    return render_template('modules/permissions/index.html', permissions=permissions)

@permission.route('/create', methods=['GET', ['POST']])
def create():
    form = FormPermission(request.form)
    return render_template('modules/permissions/create.html', form=form)

