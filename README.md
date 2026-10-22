# PoliRestaurante — Sistema de Gestión de Pedidos

## Stack
- **Backend:** Python 3.11 + Flask
- **Frontend:** HTML + Bootstrap 5 + Bootstrap Icons
- **Base de datos:** MySQL 8+
- **ORM:** SQLAlchemy

## Estructura del proyecto

```
Proyecto/
├── app/
│   ├── __init__.py              # Factory de la app Flask
│   ├── config.py                # Configuración (lee .env)
│   ├── extensions.py            # SQLAlchemy + LoginManager
│   ├── models/                  # Modelos de la BD (roles separados)
│   │   ├── usuario.py           # Base abstracta para todos los roles
│   │   ├── administrador.py     # Rol Administrador
│   │   ├── mesero.py            # Rol Mesero
│   │   ├── cocina.py            # Rol Cocina
│   │   ├── cliente.py           # Rol Cliente
│   │   ├── mesa.py
│   │   ├── categoria.py
│   │   ├── producto.py
│   │   ├── pedido.py
│   │   ├── pedido_mesa.py       # Relación N:M entre Pedido y Mesa
│   │   ├── detalle_pedido.py
│   │   ├── domicilio.py         # Para pedidos a domicilio
│   │   └── pago.py              # Control de pagos
│   ├── routes/                  # Blueprints por rol
│   │   ├── auth.py              # Login/logout con búsqueda multi-rol
│   │   ├── mesero.py            # Gestión de pedidos
│   │   ├── cocina.py            # Cola de preparación
│   │   └── admin.py             # Administración del sistema
│   └── templates/               # Vistas HTML (Jinja2 + Bootstrap 5)
│       ├── base.html
│       ├── auth/
│       ├── mesero/
│       ├── cocina/
│       └── admin/
├── database/
│   ├── schema.sql               # Esquema refactorizado + datos iniciales
│   └── seed_admin.py            # Script para crear usuario administrador
├── .env                         # Variables de entorno (NO subir a git)
├── requirements.txt
└── run.py                       # Punto de entrada
```

## Instalación y ejecución

### 1. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate        # Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar base de datos
Edita `.env` con tus credenciales MySQL, luego ejecuta el esquema:
```bash
mysql -u root -p < database/schema.sql
```

### 4. Crear usuario administrador
```bash
python database/seed_admin.py
```

### 5. Correr la aplicación
```bash
python run.py
```

Abre `http://localhost:5000` y entra con:
- **Email:** admin@polirestaurante.com
- **Password:** admin123

## Roles del sistema
| Rol     | Acceso                                        |
|---------|-----------------------------------------------|
| admin   | Dashboard, usuarios, productos, mesas + todo  |
| mesero  | Crear pedidos, ver estado, marcar entregados  |
| cocina  | Ver cola, cambiar estado (preparación → listo)|

## Documentación Scrum

El backlog del producto, los requisitos funcionales, las historias de usuario, los criterios de aceptación y la planificación por sprints están en [backlog-scrum.md](backlog-scrum.md).

Los mockups visuales correspondientes al Sprint 1 están en [mockups-sprint-1.html](mockups-sprint-1.html). Ábrelos en el navegador para tomar las capturas que se incluirán en el informe final.

Para la presentación actual utiliza [entrega-sprint-1.md](entrega-sprint-1.md), que contiene únicamente el alcance, requisitos, historias, backlog y pantallas del Sprint 1. El archivo completo queda como planificación de las próximas entregas.
