from app import db

class Base(db.Model):

    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    created_at  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

class Role(Base):
    __tablename__ = 'roles'
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name      = name
        self.description   = description

class UserRole(db.Model):
    __tablename__ = 'user_has_roles'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)

class RolePermission(db.Model):
    __tablename__ = 'role_has_permissions'
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
