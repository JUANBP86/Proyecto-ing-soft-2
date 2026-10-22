# PoliRestaurante - Entrega Sprint 1

## Alcance de esta entrega

Esta entrega presenta únicamente el trabajo realizado durante el Sprint 1: acceso al sistema y configuración inicial del restaurante.

Las funcionalidades de pedidos, cocina, pagos, domicilios e historial de clientes quedan planificadas para entregas posteriores y no forman parte de esta presentación.

## Objetivo del Sprint 1

Implementar la base administrativa del sistema para permitir el acceso de los usuarios y configurar la información inicial del restaurante.

## Funcionalidades desarrolladas

| ID | Funcionalidad | Estado |
|---|---|---|
| RF-01 | Inicio y cierre de sesión según el rol del usuario. | Implementado |
| RF-02 | Restricción de vistas según los permisos del rol. | Parcial |
| RF-03 | Creación de usuarios con diferentes roles. | Implementado |
| RF-04 | Consulta de usuarios registrados. | Implementado |
| RF-05 | Registro de productos con nombre, precio, categoría y disponibilidad. | Implementado |
| RF-06 | Consulta y gestión de productos del menú. | Parcial |
| RF-07 | Consulta de mesas, capacidad y estado. | Implementado |

## Historias de usuario

### HU-01 - Inicio de sesión

**Como** usuario registrado, **quiero** iniciar sesión con mi correo y contraseña, **para** acceder a las funciones correspondientes a mi rol.

**Criterios de aceptación:**

- Las credenciales válidas permiten el acceso.
- Las credenciales inválidas muestran un mensaje de error.
- Los usuarios inactivos no pueden ingresar.

### HU-02 - Administración de usuarios

**Como** administrador, **quiero** crear y consultar usuarios por rol, **para** controlar el acceso al sistema.

**Criterios de aceptación:**

- El formulario solicita nombre, correo, contraseña y rol.
- No se permiten correos repetidos.
- Solo el administrador puede acceder a esta función.

### HU-03 - Gestión de productos

**Como** administrador, **quiero** registrar y gestionar productos, **para** mantener actualizado el menú.

**Criterios de aceptación:**

- El producto requiere nombre, precio y categoría.
- Se puede indicar si el producto está disponible.
- Los productos no disponibles no deben aparecer en nuevos pedidos.

### HU-04 - Consulta de mesas

**Como** administrador o mesero, **quiero** consultar las mesas y su estado, **para** conocer cuáles están disponibles.

**Criterios de aceptación:**

- Se muestra el número y la capacidad de cada mesa.
- Se muestra si la mesa está disponible u ocupada.
- Las mesas ocupadas no pueden seleccionarse para nuevos pedidos.

## Product Backlog del Sprint 1

| Orden | Historia | Prioridad | Puntos | Estado |
|---:|---|---|---:|---|
| 1 | HU-01 - Inicio de sesión | Must | 3 | Implementado |
| 2 | HU-02 - Administración de usuarios | Must | 5 | Implementado |
| 3 | HU-03 - Gestión de productos | Must | 5 | Parcial |
| 4 | HU-04 - Consulta de mesas | Should | 3 | Parcial |

## Mockups incluidos

Los mockups visuales de esta entrega están en [mockups-sprint-1.html](mockups-sprint-1.html).

Incluyen únicamente las siguientes pantallas:

1. Inicio de sesión.
2. Dashboard del administrador.
3. Gestión de usuarios.
4. Creación de usuario.
5. Gestión de productos.
6. Creación de producto.
7. Estado de mesas.

## Rutas para la demostración

Durante la presentación se deben mostrar únicamente estas pantallas:

- `/auth/login`
- `/admin/`
- `/admin/usuarios`
- `/admin/usuarios/nuevo`
- `/admin/productos`
- `/admin/productos/nuevo`
- `/admin/mesas`

## Resultado del Sprint 1

Se implementó la base administrativa de PoliRestaurante. El administrador puede iniciar sesión, crear y consultar usuarios, registrar productos y consultar el estado de las mesas.

## Trabajo de próximas entregas

Las siguientes funcionalidades no se presentan como parte del Sprint 1:

- Registro y seguimiento de pedidos.
- Cola de preparación en cocina.
- Entrega de pedidos.
- Registro de pagos.
- Pedidos a domicilio.
- Historial del cliente.

## Conclusión

El Sprint 1 establece la configuración inicial necesaria para que el restaurante pueda comenzar a operar. Los siguientes sprints ampliarán el sistema con el flujo completo de pedidos y servicios adicionales.
