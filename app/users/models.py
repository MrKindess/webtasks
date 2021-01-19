from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Base(db.Model):

    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class User(Base):
    __tablename__ = 'users'
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    avatar = db.Column(db.String(), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(100),  nullable=False)
    status   = db.Column(db.Boolean, default=True)

    def __init__(self, first_name, last_name, email, avatar, phone, password):
        self.first_name = first_name
        self.last_name  = last_name
        self.avatar     = avatar
        self.phone      = phone
        self.email      = email
        self.password   = password
