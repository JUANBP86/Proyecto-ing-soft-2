"""
Script para crear el usuario administrador inicial.
Ejecutar UNA sola vez después de crear las tablas:

    python database/seed_admin.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models.administrador import Administrador

app = create_app()

with app.app_context():
    if not Administrador.query.filter_by(email='admin@polirestaurante.com').first():
        admin = Administrador(nombre='Administrador', email='admin@polirestaurante.com')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('✅  Usuario admin creado: admin@polirestaurante.com / admin123')
    else:
        print('ℹ️   El usuario admin ya existe.')
