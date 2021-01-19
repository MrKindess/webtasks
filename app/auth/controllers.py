# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.auth.forms import LoginForm
from app.users.models import User

auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/login', methods=['GET', 'POST'])
def login():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/login.html", form=form)