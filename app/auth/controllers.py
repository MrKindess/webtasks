# Import flask dependencies
import bcrypt
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask_login.utils import login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.auth.forms import LoginForm
from app.users.models import User
from flask_login import current_user, login_user, logout_user


auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # if current_user.is_authenticated:
    #     return redirect(url_for('dashboard.index'))
    #
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         user = User.query.filter_by(email=form.email.data).first()
    #         if user:
    #             if not user.status:
    #                 flash("""User has not been granted access to the system!
    #                           Please contact the system administrator""",
    #                       'danger')
    #             elif not bcrypt.check_password_hash(user.password, form.password.data):
    #                 flash('Invalid Password!', 'danger')
    #             else:
    #                 login_user(user, remember=form.remember.data)
    #                 next_page = request.args.get('next')
    #                 return redirect(next_page) if next_page else redirect(url_for('dashboard.index'))
    #         else:
    #             flash('User does not exist! Please contact the system administrator', 'danger')

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            try:
                data = User.query.filter_by(email=email).first()
                if data is not None:
                    session['logged_in'] = True
                    return redirect(url_for('dashboard.index'))
                else:
                    return 'Dont Login'
            except:
                return "Dont Login"

    return render_template("auth/login.html", form=form)



@auth.route('/logout')
def logout():
    if session.get('was_once_logged_in'):
        del session['was_once_logged_in']
    flash('You have successfully logged yourself out.')
    return redirect('/login')