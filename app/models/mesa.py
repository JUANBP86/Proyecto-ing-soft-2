from ..extensions import db


class Mesa(db.Model):
    __tablename__ = 'mesas'

    id        = db.Column(db.Integer, primary_key=True)
    numero    = db.Column(db.Integer, unique=True, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False, default=4)
    estado    = db.Column(db.Enum('disponible', 'ocupada'), default='disponible')

    pedido_mesas = db.relationship('PedidoMesa', back_populates='mesa', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Mesa {self.numero}>'
