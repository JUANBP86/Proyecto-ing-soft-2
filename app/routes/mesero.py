from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..extensions import db
from ..models.pedido import Pedido
from ..models.pedido_mesa import PedidoMesa
from ..models.mesa import Mesa
from ..models.producto import Producto
from ..models.categoria import Categoria
from ..models.detalle_pedido import DetallePedido
from ..models.mesero import Mesero
from ..models.administrador import Administrador

mesero_bp = Blueprint('mesero', __name__)


def require_mesero(f):
    """Decorador: solo permite acceso al rol mesero."""
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isinstance(current_user, (Mesero, Administrador)):
            flash('Acceso no autorizado.', 'danger')
            return redirect(url_for('auth.dashboard'))
        return f(*args, **kwargs)
    return decorated


@mesero_bp.route('/')
@login_required
@require_mesero
def index():
    # Mostrar pedidos activos del mesero actual
    if isinstance(current_user, Administrador):
        # Admin ve todos los pedidos activos
        pedidos_activos = Pedido.query.filter(
            Pedido.estado.in_(['pendiente', 'en_preparacion', 'listo'])
        ).order_by(Pedido.created_at.desc()).all()
    else:
        # Mesero ve solo sus pedidos
        pedidos_activos = Pedido.query.filter(
            Pedido.mesero_id == current_user.id,
            Pedido.estado.in_(['pendiente', 'en_preparacion', 'listo'])
        ).order_by(Pedido.created_at.desc()).all()
    return render_template('mesero/index.html', pedidos=pedidos_activos)


@mesero_bp.route('/nuevo-pedido', methods=['GET', 'POST'])
@login_required
@require_mesero
def nuevo_pedido():
    mesas      = Mesa.query.filter_by(estado='disponible').all()
    categorias = Categoria.query.all()
    productos  = Producto.query.filter_by(disponible=True).all()

    if request.method == 'POST':
        tipo          = request.form.get('tipo', 'salon')
        mesa_id       = request.form.get('mesa_id') or None
        observaciones = request.form.get('observaciones', '')
        productos_ids = request.form.getlist('producto_id')
        cantidades    = request.form.getlist('cantidad')
        notas         = request.form.getlist('nota')

        if not productos_ids:
            flash('Debe agregar al menos un producto al pedido.', 'warning')
            return render_template('mesero/nuevo_pedido.html',
                                   mesas=mesas, categorias=categorias, productos=productos)

        mesero_id = current_user.id if isinstance(current_user, Mesero) else None
        pedido = Pedido(
            tipo=tipo,
            mesero_id=mesero_id,
            observaciones=observaciones
        )
        db.session.add(pedido)
        db.session.flush()  # obtenemos el id antes del commit

        for pid, cant, nota in zip(productos_ids, cantidades, notas):
            producto = Producto.query.get(int(pid))
            if producto:
                detalle = DetallePedido(
                    pedido_id=pedido.id,
                    producto_id=producto.id,
                    cantidad=int(cant),
                    precio_unit=producto.precio,
                    subtotal=producto.precio * int(cant),
                    nota=nota
                )
                db.session.add(detalle)

        # Asociar mesa(s) si es pedido en salón
        if tipo == 'salon' and mesa_id:
            mesa = Mesa.query.get(int(mesa_id))
            if mesa:
                pedido_mesa = PedidoMesa(pedido_id=pedido.id, mesa_id=mesa.id)
                db.session.add(pedido_mesa)
                mesa.estado = 'ocupada'

        pedido.calcular_total()
        db.session.commit()
        flash(f'Pedido #{pedido.id} creado exitosamente.', 'success')
        return redirect(url_for('mesero.index'))

    return render_template('mesero/nuevo_pedido.html',
                           mesas=mesas, categorias=categorias, productos=productos)


@mesero_bp.route('/pedido/<int:pedido_id>')
@login_required
@require_mesero
def ver_pedido(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    return render_template('mesero/ver_pedido.html', pedido=pedido)


@mesero_bp.route('/pedido/<int:pedido_id>/entregar', methods=['POST'])
@login_required
@require_mesero
def entregar_pedido(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    if pedido.estado == 'listo':
        pedido.estado = 'entregado'
        # Liberar mesas asociadas solo si no hay otros pedidos activos
        for pm in pedido.mesas_pedido:
            mesa = pm.mesa
            # Verificar si hay otros pedidos activos en esta mesa
            otros_activos = Pedido.query.join(PedidoMesa).filter(
                PedidoMesa.mesa_id == mesa.id,
                Pedido.id != pedido.id,
                Pedido.estado.in_(['pendiente', 'en_preparacion', 'listo'])
            ).count()
            if otros_activos == 0:
                mesa.estado = 'disponible'
        db.session.commit()
        flash(f'Pedido #{pedido.id} marcado como entregado.', 'success')
    else:
        flash('El pedido aún no está listo para entregar.', 'warning')
    return redirect(url_for('mesero.index'))
