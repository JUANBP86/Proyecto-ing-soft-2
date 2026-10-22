from flask import Flask
from .config import Config
from .extensions import db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Registrar blueprints
    from .routes.auth import auth_bp
    from .routes.mesero import mesero_bp
    from .routes.cocina import cocina_bp
    from .routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(mesero_bp, url_prefix='/mesero')
    app.register_blueprint(cocina_bp, url_prefix='/cocina')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
