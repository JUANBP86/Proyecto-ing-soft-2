from ..extensions import db
from datetime import datetime


class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id            = db.Column(db.Integer, primary_key=True)
    tipo          = db.Column(db.Enum('salon', 'para_llevar', 'domicilio'), nullable=False, default='salon')
    estado        = db.Column(
        db.Enum('pendiente', 'en_preparacion', 'listo', 'entregado', 'cancelado'),
        nullable=False,
        default='pendiente'
    )
    observaciones = db.Column(db.Text)
    total         = db.Column(db.Numeric(10, 2), default=0.00)

    cliente_id    = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=True)
    mesero_id     = db.Column(db.Integer, db.ForeignKey('meseros.id'), nullable=True)

    created_at    = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at    = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    detalles      = db.relationship('DetallePedido', backref='pedido', lazy=True, cascade='all, delete-orphan')
    mesas_pedido  = db.relationship('PedidoMesa', back_populates='pedido', cascade='all, delete-orphan')
    domicilio     = db.relationship('Domicilio', back_populates='pedido', uselist=False, cascade='all, delete-orphan')
    pagos         = db.relationship('Pago', back_populates='pedido', cascade='all, delete-orphan')

    def calcular_total(self):
        self.total = sum(float(d.subtotal) for d in self.detalles)

    def __repr__(self):
        return f'<Pedido #{self.id} [{self.estado}]>'
