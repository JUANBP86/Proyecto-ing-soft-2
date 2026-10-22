# Backlog Scrum - PoliRestaurante

## 1. Visión del producto

PoliRestaurante es un sistema web para gestionar el menú, los usuarios, las mesas y el ciclo de vida de los pedidos de un restaurante. El sistema debe conectar el trabajo del administrador, mesero y cocina, manteniendo información consistente sobre disponibilidad, estados y pagos.

## 2. Objetivo del producto

Permitir que un restaurante registre y controle sus pedidos de salón, para llevar y a domicilio desde un solo sistema, reduciendo errores en la toma de órdenes y mejorando el seguimiento de cada pedido.

## 3. Actores

| Actor | Necesidad principal |
|---|---|
| Administrador | Configurar usuarios, productos, categorías y mesas; consultar indicadores. |
| Mesero | Crear pedidos, asociarlos a mesas y entregarlos cuando estén listos. |
| Cocina | Consultar la cola de pedidos y actualizar su estado de preparación. |
| Cliente | Consultar el menú, realizar pedidos y conocer el estado de su compra. |
| Sistema | Validar permisos, calcular totales, conservar el historial y evitar datos inconsistentes. |

## 4. Requisitos funcionales

| ID | Requisito | Prioridad | Estado actual |
|---|---|---|---|
| RF-01 | El sistema debe permitir iniciar y cerrar sesión según el rol del usuario. | Must | Implementado |
| RF-02 | El sistema debe restringir cada vista y operación según los permisos del rol. | Must | Parcial |
| RF-03 | El administrador debe crear usuarios con rol de administrador, mesero, cocina o cliente. | Must | Implementado |
| RF-04 | El administrador debe consultar el listado de usuarios registrados. | Should | Implementado |
| RF-05 | El administrador debe registrar productos con nombre, descripción, precio, categoría y disponibilidad. | Must | Implementado |
| RF-06 | El administrador debe consultar el menú y activar o desactivar productos. | Must | Parcial |
| RF-07 | El administrador debe consultar las mesas, su capacidad y su estado. | Must | Implementado |
| RF-08 | El mesero debe crear pedidos de salón, para llevar o a domicilio. | Must | Parcial |
| RF-09 | El mesero debe agregar uno o más productos, cantidades y notas a un pedido. | Must | Implementado |
| RF-10 | El sistema debe calcular automáticamente el subtotal de cada detalle y el total del pedido. | Must | Implementado |
| RF-11 | El sistema debe asociar los pedidos de salón con una mesa disponible y actualizar su estado. | Must | Implementado |
| RF-12 | Cocina debe consultar la cola de pedidos pendientes y en preparación ordenada por antigüedad. | Must | Implementado |
| RF-13 | Cocina debe cambiar el estado de un pedido de pendiente a en preparación y luego a listo. | Must | Implementado |
| RF-14 | El mesero debe consultar el detalle y el estado de sus pedidos activos. | Must | Implementado |
| RF-15 | El mesero debe marcar como entregado un pedido que esté listo. | Must | Implementado |
| RF-16 | El sistema debe liberar una mesa cuando no tenga otros pedidos activos asociados. | Must | Implementado |
| RF-17 | El cliente debe registrarse y consultar los productos disponibles por categoría. | Should | Pendiente |
| RF-18 | El cliente debe crear pedidos a domicilio con dirección y referencia de entrega. | Should | Pendiente |
| RF-19 | El cliente o el mesero debe registrar el método y el estado del pago. | Must | Pendiente |
| RF-20 | El cliente debe consultar el estado y el historial de sus pedidos. | Should | Pendiente |
| RF-21 | El administrador debe consultar indicadores de pedidos totales, pedidos del día y pedidos activos. | Should | Implementado |
| RF-22 | El sistema debe validar datos obligatorios, precios, cantidades positivas, estados y transiciones permitidas. | Must | Parcial |
| RF-23 | El sistema debe conservar fecha de creación y actualización de los pedidos. | Must | Implementado |
| RF-24 | El sistema debe impedir el acceso a información o acciones no autorizadas. | Must | Parcial |

## 5. Historias de usuario

### Épica E1 - Acceso y usuarios

#### HU-01 - Iniciar sesión

**Como** usuario registrado, **quiero** iniciar sesión con mi correo y contraseña, **para** acceder a las funciones correspondientes a mi rol.

**Criterios de aceptación**

- Dado un usuario activo con credenciales válidas, cuando inicia sesión, entonces es enviado a su panel correspondiente.
- Dadas credenciales inválidas, cuando intenta iniciar sesión, entonces el sistema muestra un mensaje de error y no crea una sesión.
- Un usuario inactivo no puede iniciar sesión.

**Prioridad:** Must | **Estimación:** 3 puntos | **Relacionada:** RF-01

#### HU-02 - Administrar usuarios

**Como** administrador, **quiero** crear y consultar usuarios por rol, **para** controlar quién puede operar el sistema.

**Criterios de aceptación**

- El formulario solicita nombre, correo, contraseña y rol.
- El sistema rechaza un correo ya registrado.
- El usuario creado puede iniciar sesión con el rol asignado.
- Solo un administrador puede acceder a esta funcionalidad.

**Prioridad:** Must | **Estimación:** 5 puntos | **Relacionadas:** RF-02, RF-03, RF-04

### Épica E2 - Menú y configuración

#### HU-03 - Gestionar productos disponibles

**Como** administrador, **quiero** registrar y gestionar productos del menú, **para** mantener actualizada la oferta del restaurante.

**Criterios de aceptación**

- El producto requiere nombre, precio válido y categoría.
- Un producto marcado como no disponible no aparece al crear un pedido.
- El precio guardado se usa para calcular el pedido.
- Solo un administrador puede crear o cambiar productos.

**Prioridad:** Must | **Estimación:** 5 puntos | **Relacionadas:** RF-05, RF-06

#### HU-04 - Consultar estado de mesas

**Como** administrador o mesero, **quiero** consultar las mesas y su estado, **para** asignar pedidos sin ocupar una mesa en uso.

**Criterios de aceptación**

- Se muestran número, capacidad y estado de cada mesa.
- Una mesa ocupada no puede seleccionarse para un nuevo pedido de salón.
- Al entregar el último pedido activo de una mesa, esta vuelve a estar disponible.

**Prioridad:** Must | **Estimación:** 3 puntos | **Relacionada:** RF-07, RF-11, RF-16

### Épica E3 - Gestión de pedidos

#### HU-05 - Registrar pedido

**Como** mesero, **quiero** registrar un pedido con productos, cantidades y observaciones, **para** enviarlo correctamente a cocina.

**Criterios de aceptación**

- El pedido contiene al menos un producto.
- Cada detalle guarda producto, cantidad, precio unitario, subtotal y nota opcional.
- El sistema calcula el total sumando los subtotales.
- Para un pedido de salón se puede asociar una mesa disponible.
- El pedido inicia en estado pendiente.

**Prioridad:** Must | **Estimación:** 8 puntos | **Relacionadas:** RF-08, RF-09, RF-10, RF-11

#### HU-06 - Consultar pedidos activos

**Como** mesero, **quiero** consultar mis pedidos activos y su detalle, **para** saber cuáles debo entregar o atender.

**Criterios de aceptación**

- Se muestran los pedidos del mesero en estados pendiente, en preparación o listo.
- El detalle muestra productos, cantidades, notas, total y estado.
- Un administrador puede consultar todos los pedidos activos.

**Prioridad:** Must | **Estimación:** 3 puntos | **Relacionada:** RF-14

#### HU-07 - Entregar pedido

**Como** mesero, **quiero** marcar como entregado un pedido listo, **para** cerrar correctamente el servicio.

**Criterios de aceptación**

- Solo un pedido en estado listo puede marcarse como entregado.
- Un pedido pendiente o en preparación no puede entregarse.
- Al entregar, el sistema libera las mesas que ya no tengan pedidos activos.

**Prioridad:** Must | **Estimación:** 3 puntos | **Relacionada:** RF-15, RF-16

### Épica E4 - Preparación en cocina

#### HU-08 - Gestionar cola de cocina

**Como** usuario de cocina, **quiero** ver los pedidos pendientes ordenados por llegada, **para** preparar primero los más antiguos.

**Criterios de aceptación**

- La cola incluye pedidos pendientes y en preparación.
- Los pedidos se ordenan del más antiguo al más reciente.
- Cocina puede iniciar la preparación de un pedido pendiente.

**Prioridad:** Must | **Estimación:** 5 puntos | **Relacionada:** RF-12

#### HU-09 - Marcar pedido como listo

**Como** usuario de cocina, **quiero** marcar un pedido en preparación como listo, **para** notificar al mesero que puede entregarlo.

**Criterios de aceptación**

- Solo se permite la transición pendiente -> en preparación -> listo.
- No se permiten saltos de estado ni retrocesos desde la interfaz.
- El cambio queda persistido y es visible para el mesero.

**Prioridad:** Must | **Estimación:** 3 puntos | **Relacionada:** RF-13

### Épica E5 - Domicilios y pagos

#### HU-10 - Registrar domicilio

**Como** cliente, **quiero** indicar mi dirección y referencia, **para** recibir mi pedido a domicilio.

**Criterios de aceptación**

- La dirección es obligatoria.
- La referencia es opcional.
- El domicilio queda asociado a un único pedido y comienza en estado pendiente.
- El pedido se identifica como domicilio.

**Prioridad:** Should | **Estimación:** 8 puntos | **Relacionada:** RF-18

#### HU-11 - Registrar pago

**Como** cliente o mesero, **quiero** registrar el método y monto del pago, **para** conocer si el pedido fue pagado.

**Criterios de aceptación**

- El método solo puede ser efectivo, tarjeta, transferencia o QR.
- El monto debe ser positivo y corresponder al total del pedido.
- El pago inicia como pendiente y puede cambiar a pagado o rechazado.
- Un pedido no puede cerrarse como pagado sin un pago aprobado.

**Prioridad:** Must | **Estimación:** 8 puntos | **Relacionada:** RF-19

#### HU-12 - Consultar historial del cliente

**Como** cliente, **quiero** consultar mis pedidos anteriores y su estado, **para** hacer seguimiento de mis compras.

**Criterios de aceptación**

- El cliente solo puede consultar sus propios pedidos.
- Se muestran fecha, tipo, total y estado.
- El cliente puede abrir el detalle de cada pedido.

**Prioridad:** Should | **Estimación:** 5 puntos | **Relacionada:** RF-20

### Épica E6 - Control y calidad

#### HU-13 - Consultar indicadores

**Como** administrador, **quiero** consultar indicadores básicos de operación, **para** conocer el estado del restaurante.

**Criterios de aceptación**

- El panel muestra pedidos totales, pedidos del día y pedidos activos.
- Los valores se calculan con datos persistidos.
- Solo un administrador puede consultar el panel.

**Prioridad:** Should | **Estimación:** 3 puntos | **Relacionada:** RF-21

#### HU-14 - Validar operaciones

**Como** responsable del sistema, **quiero** que las operaciones validen datos y permisos, **para** evitar registros inconsistentes o accesos indebidos.

**Criterios de aceptación**

- Los campos obligatorios y numéricos inválidos generan un mensaje claro.
- No se pueden crear pedidos sin productos ni con cantidades menores que uno.
- Las operaciones protegidas requieren autenticación y rol autorizado.
- Las transiciones de estado inválidas son rechazadas.

**Prioridad:** Must | **Estimación:** 5 puntos | **Relacionadas:** RF-22, RF-24

## 6. Product backlog priorizado

La prioridad sigue la escala **Must**, **Should** y **Could**. La estimación usa puntos de historia relativos: 1, 2, 3, 5 y 8.

| Orden | ID | Ítem del backlog | Prioridad | Puntos | Estado |
|---:|---|---|---|---:|---|
| 1 | HU-01 | Inicio y cierre de sesión | Must | 3 | Implementado |
| 2 | HU-02 | Administración de usuarios y roles | Must | 5 | Implementado |
| 3 | HU-03 | Gestión de productos y disponibilidad | Must | 5 | Parcial |
| 4 | HU-05 | Registro de pedidos | Must | 8 | Implementado |
| 5 | HU-08 | Cola de cocina | Must | 5 | Implementado |
| 6 | HU-09 | Estados de preparación | Must | 3 | Implementado |
| 7 | HU-06 | Consulta de pedidos activos | Must | 3 | Implementado |
| 8 | HU-07 | Entrega y liberación de mesas | Must | 3 | Implementado |
| 9 | HU-14 | Validaciones y autorización | Must | 5 | Parcial |
| 10 | HU-11 | Registro de pagos | Must | 8 | Pendiente |
| 11 | HU-04 | Consulta y administración de mesas | Should | 3 | Parcial |
| 12 | HU-13 | Indicadores administrativos | Should | 3 | Implementado |
| 13 | HU-10 | Pedidos a domicilio | Should | 8 | Pendiente |
| 14 | HU-12 | Historial del cliente | Should | 5 | Pendiente |

## 7. Plan sugerido de sprints

### Sprint 1 - Acceso y configuración

**Objetivo:** dejar lista la administración básica y el acceso seguro.

- HU-01, HU-02, HU-03 y HU-04.
- Validar autenticación, roles, productos, categorías y mesas.
- Entregable: administrador puede preparar el sistema para operar.

### Sprint 2 - Pedido y cocina

**Objetivo:** completar el flujo principal desde la toma del pedido hasta su preparación.

- HU-05, HU-06, HU-08 y HU-09.
- Validar cálculo de totales y transiciones de estado.
- Entregable: un pedido puede pasar de pendiente a listo.

### Sprint 3 - Entrega y control

**Objetivo:** cerrar el flujo presencial y reforzar la integridad del sistema.

- HU-07, HU-13 y HU-14.
- Validar entrega, liberación de mesas, permisos y datos inválidos.
- Entregable: flujo de salón completo y controlado.

### Sprint 4 - Pagos y domicilios

**Objetivo:** ampliar el sistema para pedidos externos y cierre financiero.

- HU-10, HU-11 y HU-12.
- Validar domicilios, pagos e historial por cliente.
- Entregable: ciclo completo de pedido a domicilio con seguimiento.

## 8. Definición de terminado

Una historia se considera terminada cuando:

- Cumple todos sus criterios de aceptación.
- El código está integrado en la aplicación sin romper los flujos existentes.
- La información se guarda y consulta correctamente en MySQL.
- Se validan permisos, datos obligatorios y errores esperados.
- Se prueba el flujo principal con los roles involucrados.
- La interfaz muestra mensajes comprensibles para éxito y error.
- Se actualiza la documentación cuando cambia el comportamiento del sistema.

## 9. Riesgos y supuestos

- Se asume que MySQL 8+ es el motor oficial y que la conexión se configura mediante `.env`.
- Los pagos no deben considerarse realmente aprobados hasta definir si habrá integración con una pasarela externa o registro manual.
- Los pedidos a domicilio requieren decidir quién asigna el pedido a reparto y cómo se actualiza el estado `en_ruta`.
- Debe definirse una política para cancelar pedidos y para modificar productos después de enviarlos a cocina.
- Las pruebas de aceptación deben ejecutarse con al menos un usuario de cada rol.
