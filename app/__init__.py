from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)

# cấu hình kết nối sql
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Goby@123@localhost/webtask'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://['tài khoản mysql']:[mật khẩu mysql]@localhost/[ten-database]'
db = SQLAlchemy(app)

# xử lý lỗi ngoại lệ
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.auth.controllers import auth
from app.users.controllers import users
from app.dashboard.controllers import dashboard
#from app.permission.controllers import permissions
from app.roles.controllers import roles

# Register blueprint(s)
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(users)
#app.register_blueprint(permissions)
app.register_blueprint(roles)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()