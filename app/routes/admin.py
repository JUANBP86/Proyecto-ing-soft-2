from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..extensions import db
from ..models.administrador import Administrador
from ..models.mesero import Mesero
from ..models.cocina import Cocina
from ..models.cliente import Cliente
from ..models.producto import Producto
from ..models.categoria import Categoria
from ..models.mesa import Mesa
from ..models.pedido import Pedido

admin_bp = Blueprint('admin', __name__)


def require_admin(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isinstance(current_user, Administrador):
            flash('Acceso restringido a administradores.', 'danger')
            return redirect(url_for('auth.dashboard'))
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/')
@login_required
@require_admin
def index():
    total_pedidos  = Pedido.query.count()
    pedidos_hoy    = Pedido.query.filter(
        db.func.date(Pedido.created_at) == db.func.current_date()
    ).count()
    pedidos_activos = Pedido.query.filter(
        Pedido.estado.in_(['pendiente', 'en_preparacion', 'listo'])
    ).count()
    return render_template('admin/index.html',
                           total_pedidos=total_pedidos,
                           pedidos_hoy=pedidos_hoy,
                           pedidos_activos=pedidos_activos)


# ── Usuarios ──────────────────────────────────────────────
@admin_bp.route('/usuarios')
@login_required
@require_admin
def usuarios():
    lista = []
    for modelo in (Administrador, Mesero, Cocina, Cliente):
        lista.extend(modelo.query.all())
    return render_template('admin/usuarios.html', usuarios=lista)


@admin_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
@login_required
@require_admin
def nuevo_usuario():
    if request.method == 'POST':
        nombre   = request.form.get('nombre', '').strip()
        email    = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        rol      = request.form.get('rol')

        modelos = {
            'admin': Administrador,
            'mesero': Mesero,
            'cocina': Cocina,
            'cliente': Cliente,
        }

        modelo = modelos.get(rol)
        if modelo and modelo.query.filter_by(email=email).first():
            flash('Ya existe un usuario con ese email.', 'danger')
        else:
            if modelo is None:
                flash('Rol inválido.', 'danger')
                return render_template('admin/nuevo_usuario.html')
            u = modelo(nombre=nombre, email=email)
            u.set_password(password)
            db.session.add(u)
            db.session.commit()
            flash('Usuario creado correctamente.', 'success')
            return redirect(url_for('admin.usuarios'))

    return render_template('admin/nuevo_usuario.html')


# ── Productos ─────────────────────────────────────────────
@admin_bp.route('/productos')
@login_required
@require_admin
def productos():
    lista = Producto.query.all()
    return render_template('admin/productos.html', productos=lista)


@admin_bp.route('/productos/nuevo', methods=['GET', 'POST'])
@login_required
@require_admin
def nuevo_producto():
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nombre       = request.form.get('nombre', '').strip()
        descripcion  = request.form.get('descripcion', '')
        precio       = request.form.get('precio')
        categoria_id = request.form.get('categoria_id')
        disponible   = request.form.get('disponible') == 'on'

        p = Producto(nombre=nombre, descripcion=descripcion,
                     precio=precio, categoria_id=categoria_id,
                     disponible=disponible)
        db.session.add(p)
        db.session.commit()
        flash('Producto agregado.', 'success')
        return redirect(url_for('admin.productos'))

    return render_template('admin/nuevo_producto.html', categorias=categorias)


# ── Mesas ─────────────────────────────────────────────────
@admin_bp.route('/mesas')
@login_required
@require_admin
def mesas():
    lista = Mesa.query.order_by(Mesa.numero).all()
    return render_template('admin/mesas.html', mesas=lista)
