from ..extensions import db
from .usuario import Usuario


class Cliente(Usuario):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(30), nullable=True)
    activo = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)
    domicilios = db.relationship('Domicilio', backref='cliente', lazy=True)

    def __repr__(self):
        return f'<Cliente {self.nombre}>'
