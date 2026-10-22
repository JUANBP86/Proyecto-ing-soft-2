from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from ..models.administrador import Administrador
from ..models.mesero import Mesero
from ..models.cocina import Cocina
from ..models.cliente import Cliente

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')

        usuario = None
        for model in (Administrador, Mesero, Cocina, Cliente):
            usuario = model.query.filter_by(email=email, activo=True).first()
            if usuario:
                break

        if usuario and usuario.check_password(password):
            login_user(usuario)
            flash(f'Bienvenido, {usuario.nombre}!', 'success')
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Credenciales incorrectas.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol == 'mesero':
        return redirect(url_for('mesero.index'))
    elif current_user.rol == 'cocina':
        return redirect(url_for('cocina.index'))
    elif current_user.rol == 'admin':
        return redirect(url_for('admin.index'))
    return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('auth.login'))
