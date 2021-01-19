from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.users.forms import CreateUserForm
from app.users.models import User

users = Blueprint('users', __name__, url_prefix='/users')


# Set the route and accepted methods
@users.route('/', methods=['GET'])
def index():
    users = User.query.all()
    return render_template('modules/users/index.html', users=users)


@users.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateUserForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.first_name.data
            email = form.first_name.data
            password = form.first_name.data

            users = User(first_name, last_name, email, '', '',
                         password=generate_password_hash(password))

            db.session.add(users)
            db.session.commit()

            flash('Users has been successfully created!', 'success')

            return redirect(url_for('users.index'))

        else:
            flash('Your form has errors! Please check the fields', 'danger')

    return render_template('modules/users/create.html', form=form)
