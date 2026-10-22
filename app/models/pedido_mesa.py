from ..extensions import db


class PedidoMesa(db.Model):
    __tablename__ = 'pedido_mesa'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesas.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    pedido = db.relationship('Pedido', back_populates='mesas_pedido')
    mesa = db.relationship('Mesa', back_populates='pedido_mesas')

    def __repr__(self):
        return f'<PedidoMesa pedido#{self.pedido_id} mesa#{self.mesa_id}>'
