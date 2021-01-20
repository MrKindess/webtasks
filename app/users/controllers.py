from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.users.forms import CreateUserForm, EditUserForm
from app.users.models import User

users = Blueprint('users', __name__, url_prefix='/users')


# Set the route and accepted methods
@users.route('/', methods=['GET'])
def index():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=10)

    return render_template('modules/users/index.html', users=users)


@users.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateUserForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            phone = form.phone.data
            password = form.first_name.data

            users = User(first_name, last_name, email, '', phone,
                         password=generate_password_hash(password))

            db.session.add(users)
            db.session.commit()

            flash('Users has been successfully created!', 'success')

            return redirect(url_for('users.index'))

        else:
            flash('Your form has errors! Please check the fields', 'danger')

    return render_template('modules/users/create.html', form=form)

@users.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return redirect(url_for('users.index'))

    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']
        user.phone = request.form['phone']
        user.password = request.form['password']

        try:
            db.session.commit()
            flash('The user has been successfully updated', 'success')
            return redirect(url_for('users.index'))
        except:
            flash('User update failed! Form has errors', 'danger')
    else:
        print(user)
        return render_template("modules/users/edit.html", user=user)

@users.route('/<int:id>/delete')
def delete(id):
    user = User.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('users.index'))
    abort(404)