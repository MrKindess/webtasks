from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
dashboard = Blueprint('dashboard', __name__, url_prefix='/')

@dashboard.route('/')
def index():
	return render_template('modules/dashboard/index.html')

# view page role manager
@dashboard.route('/role')
def role():
    return render_template('modules/role/index.html')

@dashboard.route('/role/create')
def createRole():
    return render_template('modules/role/create.html')

@dashboard.route('/role/edit')
def editRole():
    return render_template('modules/role/edit.html')

# view page permission manager
@dashboard.route('/permission')
def permisison():
    return render_template('modules/permission/index.html')

@dashboard.route('/permission/create')
def createPermisison():
    return render_template('modules/permission/create.html')

@dashboard.route('/permission/edit')
def editPermisison():
    return render_template('modules/permission/edit.html')

# view page job manager
@dashboard.route('/job')
def job():
    return render_template('modules/job/index.html')

@dashboard.route('/job/create')
def createJob():
    return render_template('modules/job/create.html')

@dashboard.route('/job/edit')
def editJob():
    return render_template('modules/job/edit.html')

@dashboard.route('/job/show')
def showJob():
    return render_template('modules/job/show.html')

# page category setting
@dashboard.route('/job-category')
def category():
    return render_template('modules/job_category/index.html')

# page meeting
@dashboard.route('/meeting')
def metting():
    return render_template('modules/meeting/index.html')

@dashboard.route('/meeting/create')
def createMetting():
    return render_template('modules/meeting/create.html')

@dashboard.route('/meeting/show')
def showMetting():
    return render_template('modules/meeting/show.html')