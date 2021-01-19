from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Base(db.Model):

    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Role(Base):
    __tablename__ = 'roles'
    name = db.Column(db.String())
    description = db.Column(db.String())

    def __init__(self, name, description):
        self.name      = name
        self.description   = description

class UserRole(db.Model):
    __tablename__ = 'user_has_roles'
    user_id = db.Integer, db.ForeignKey('users.id')
    role_id = db.Integer, db.ForeignKey('roles.id')

class RolePermission(db.Model):
    __tablename__ = 'role_has_permissions'
    permission_id = db.Integer, db.ForeignKey('permissions.id')
    role_id = db.Integer, db.ForeignKey('roles.id')
