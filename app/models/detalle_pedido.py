from ..extensions import db


class DetallePedido(db.Model):
    __tablename__ = 'detalle_pedidos'

    id          = db.Column(db.Integer, primary_key=True)
    pedido_id   = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad    = db.Column(db.Integer, nullable=False, default=1)
    precio_unit = db.Column(db.Numeric(10, 2), nullable=False)  # precio al momento del pedido
    subtotal    = db.Column(db.Numeric(10, 2), nullable=False)
    nota        = db.Column(db.String(255))  # ej: "sin cebolla"

    def calcular_subtotal(self):
        self.subtotal = self.cantidad * self.precio_unit

    def __repr__(self):
        return f'<Detalle pedido#{self.pedido_id} producto#{self.producto_id}>'
