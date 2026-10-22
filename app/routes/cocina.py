from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..extensions import db
from ..models.pedido import Pedido
from ..models.cocina import Cocina
from ..models.administrador import Administrador

cocina_bp = Blueprint('cocina', __name__)


def require_cocina(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isinstance(current_user, (Cocina, Administrador)):
            flash('Acceso no autorizado.', 'danger')
            return redirect(url_for('auth.dashboard'))
        return f(*args, **kwargs)
    return decorated


@cocina_bp.route('/')
@login_required
@require_cocina
def index():
    # Cocina ve pedidos pendientes y en preparación
    pedidos = Pedido.query.filter(
        Pedido.estado.in_(['pendiente', 'en_preparacion'])
    ).order_by(Pedido.created_at.asc()).all()
    return render_template('cocina/index.html', pedidos=pedidos)


@cocina_bp.route('/pedido/<int:pedido_id>/estado', methods=['POST'])
@login_required
@require_cocina
def cambiar_estado(pedido_id):
    pedido     = Pedido.query.get_or_404(pedido_id)
    nuevo_estado = request.form.get('estado')

    transiciones_validas = {
        'pendiente':      'en_preparacion',
        'en_preparacion': 'listo',
    }

    if transiciones_validas.get(pedido.estado) == nuevo_estado:
        pedido.estado = nuevo_estado
        db.session.commit()
        flash(f'Pedido #{pedido.id} actualizado a "{nuevo_estado}".', 'success')
    else:
        flash('Transición de estado no válida.', 'danger')

    return redirect(url_for('cocina.index'))
