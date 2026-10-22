from ..extensions import db


class Producto(db.Model):
    __tablename__ = 'productos'

    id           = db.Column(db.Integer, primary_key=True)
    nombre       = db.Column(db.String(120), nullable=False)
    descripcion  = db.Column(db.String(255))
    precio       = db.Column(db.Numeric(10, 2), nullable=False)
    disponible   = db.Column(db.Boolean, default=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    detalles     = db.relationship('DetallePedido', backref='producto', lazy=True)

    def __repr__(self):
        return f'<Producto {self.nombre}>'
