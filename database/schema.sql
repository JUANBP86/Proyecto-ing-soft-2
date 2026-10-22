-- ============================================================
--  PoliRestaurante — Esquema de base de datos
--  Motor: MySQL 8+
--  Modelo corrigido: Cliente, Mesero, Cocina, Administrador
--  Pedidos con relación muchos a muchos con Mesas usando pedido_mesa
-- ============================================================

CREATE DATABASE IF NOT EXISTS polirestaurante
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE polirestaurante;

-- ------------------------------------------------------------
-- Clientes
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS clientes (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    email      VARCHAR(120) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    telefono   VARCHAR(30) NULL,
    activo     TINYINT(1) NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- Administradores
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS administradores (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    email      VARCHAR(120) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    activo     TINYINT(1) NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- Meseros
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS meseros (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    email      VARCHAR(120) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    activo     TINYINT(1) NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- Cocinas
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS cocinas (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    email      VARCHAR(120) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL,
    activo     TINYINT(1) NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- ------------------------------------------------------------
-- Mesas del restaurante
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mesas (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    numero    INT NOT NULL UNIQUE,
    capacidad INT NOT NULL DEFAULT 4,
    estado    ENUM('disponible', 'ocupada') NOT NULL DEFAULT 'disponible'
);

-- ------------------------------------------------------------
-- Categorías del menú
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS categorias (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nombre      VARCHAR(80) NOT NULL UNIQUE,
    descripcion VARCHAR(255)
);

-- ------------------------------------------------------------
-- Productos del menú
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS productos (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    nombre       VARCHAR(120) NOT NULL,
    descripcion  VARCHAR(255),
    precio       DECIMAL(10,2) NOT NULL,
    disponible   TINYINT(1) NOT NULL DEFAULT 1,
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- ------------------------------------------------------------
-- Pedidos
--  Un pedido puede involucrar varias mesas y distintos tipos de servicio
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS pedidos (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    tipo          ENUM('salon', 'para_llevar', 'domicilio') NOT NULL DEFAULT 'salon',
    estado        ENUM('pendiente', 'en_preparacion', 'listo', 'entregado', 'cancelado')
                  NOT NULL DEFAULT 'pendiente',
    observaciones TEXT,
    total         DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    cliente_id    INT NULL,
    mesero_id     INT NULL,
    created_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
                  ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (mesero_id) REFERENCES meseros(id)
);

-- ------------------------------------------------------------
-- Relación muchos a muchos entre pedidos y mesas
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS pedido_mesa (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    mesa_id   INT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uq_pedido_mesa (pedido_id, mesa_id),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (mesa_id) REFERENCES mesas(id) ON DELETE CASCADE
);

-- ------------------------------------------------------------
-- Detalle de pedidos
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS detalle_pedidos (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id   INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad    INT NOT NULL DEFAULT 1,
    precio_unit DECIMAL(10,2) NOT NULL,
    subtotal    DECIMAL(10,2) NOT NULL,
    nota        VARCHAR(255),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

-- ------------------------------------------------------------
-- Domicilio del pedido
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS domicilios (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id   INT NOT NULL UNIQUE,
    cliente_id  INT NOT NULL,
    direccion   VARCHAR(255) NOT NULL,
    referencia  VARCHAR(255),
    latitud     DECIMAL(10,8),
    longitud    DECIMAL(11,8),
    estado      ENUM('pendiente', 'en_ruta', 'entregado', 'cancelado') NOT NULL DEFAULT 'pendiente',
    created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- ------------------------------------------------------------
-- Pago del pedido
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS pagos (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id  INT NOT NULL,
    metodo     ENUM('efectivo', 'tarjeta', 'transferencia', 'qr') NOT NULL,
    monto      DECIMAL(10,2) NOT NULL,
    estado     ENUM('pendiente', 'pagado', 'rechazado') NOT NULL DEFAULT 'pendiente',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE
);

-- ============================================================
--  Datos iniciales (seed)
-- ============================================================

INSERT INTO categorias (nombre, descripcion) VALUES
  ('Hamburguesas', 'Hamburguesas clásicas y especiales'),
  ('Bebidas', 'Refrescos, jugos y agua'),
  ('Acompañamientos', 'Papas, ensaladas y extras'),
  ('Postres', 'Helados, tortas y más');

INSERT INTO productos (nombre, descripcion, precio, disponible, categoria_id) VALUES
  ('Hamburguesa Clásica', 'Carne, lechuga, tomate, mostaza', 8.50, 1, 1),
  ('Hamburguesa BBQ', 'Carne, cheddar, cebolla, BBQ', 10.00, 1, 1),
  ('Hamburguesa Pollo', 'Pechuga empanizada, pepinillos', 9.00, 1, 1),
  ('Coca-Cola 500ml', '', 2.50, 1, 2),
  ('Jugo de naranja', 'Natural, 300ml', 3.00, 1, 2),
  ('Agua mineral', '500ml', 1.50, 1, 2),
  ('Papas fritas medianas', 'Crujientes con sal', 3.50, 1, 3),
  ('Papas fritas grandes', 'Crujientes con sal', 4.50, 1, 3),
  ('Helado de vainilla', 'Dos bolas', 3.00, 1, 4);

INSERT INTO mesas (numero, capacidad, estado) VALUES
  (1, 2, 'disponible'),
  (2, 4, 'disponible'),
  (3, 4, 'disponible'),
  (4, 6, 'disponible'),
  (5, 6, 'disponible');
