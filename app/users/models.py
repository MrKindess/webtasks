from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class User(Base):
    __tablename__ = 'users'
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    avatar = db.Column(db.String(50))
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50),  nullable=False)
    status   = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, first_name, last_name, email, avatar, phone, password, status):
        self.first_name = first_name
        self.last_name  = last_name
        self.avatar     = avatar
        self.phone      = phone
        self.email      = email
        self.password   = password
        self.status     = status
