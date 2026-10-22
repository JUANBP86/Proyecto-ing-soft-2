from ..extensions import db


class Domicilio(db.Model):
    __tablename__ = 'domicilios'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False, unique=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    referencia = db.Column(db.String(255), nullable=True)
    latitud = db.Column(db.Numeric(10, 8), nullable=True)
    longitud = db.Column(db.Numeric(11, 8), nullable=True)
    estado = db.Column(db.Enum('pendiente', 'en_ruta', 'entregado', 'cancelado'), default='pendiente')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    pedido = db.relationship('Pedido', back_populates='domicilio')

    def __repr__(self):
        return f'<Domicilio pedido#{self.pedido_id}>'
