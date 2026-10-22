from ..extensions import db


class Pago(db.Model):
    __tablename__ = 'pagos'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    metodo = db.Column(db.Enum('efectivo', 'tarjeta', 'transferencia', 'qr'), nullable=False)
    monto = db.Column(db.Numeric(10, 2), nullable=False)
    estado = db.Column(db.Enum('pendiente', 'pagado', 'rechazado'), default='pendiente')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    pedido = db.relationship('Pedido', back_populates='pagos')

    def __repr__(self):
        return f'<Pago pedido#{self.pedido_id}>'
