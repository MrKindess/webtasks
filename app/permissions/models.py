from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a User model
class Permission(Base):
    __tablename__ = 'permissions'
    name = db.Column(db.String())
    description = db.Column(db.String())

    def __init__(self, name, description):
        self.name = name
        self.description = description
