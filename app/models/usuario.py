from ..extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Usuario(UserMixin, db.Model):
    __abstract__ = True

    id         = db.Column(db.Integer, primary_key=True)
    nombre     = db.Column(db.String(100), nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    password   = db.Column(db.String(255), nullable=False)
    activo     = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def rol(self):
        mapping = {
            'Mesero': 'mesero',
            'Cocina': 'cocina',
            'Administrador': 'admin',
            'Cliente': 'cliente',
        }
        return mapping.get(self.__class__.__name__, self.__class__.__name__.lower())

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Usuario {self.nombre} ({self.rol})>'


@login_manager.user_loader
def load_user(user_id):
    from .cliente import Cliente
    from .mesero import Mesero
    from .cocina import Cocina
    from .administrador import Administrador

    for model in (Cliente, Mesero, Cocina, Administrador):
        user = model.query.get(int(user_id))
        if user:
            return user
    return None
