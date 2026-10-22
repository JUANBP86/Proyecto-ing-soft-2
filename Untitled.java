erDiagram
    USUARIOS ||--o{ PEDIDOS : crea
    MESAS ||--o{ PEDIDOS : atiende
    CATEGORIAS ||--o{ PRODUCTOS : contiene
    PRODUCTOS ||--o{ DETALLE_PEDIDOS : aparece_en
    PEDIDOS ||--o{ DETALLE_PEDIDOS : incluye
    CLIENTES ||--o{ PEDIDOS : realiza
    PEDIDOS ||--o| DOMICILIOS : tiene
    PEDIDOS ||--o| PAGOS : registra

    USUARIOS {
        int id PK
        varchar nombre
        varchar email
        varchar password
        enum rol
        boolean activo
        datetime created_at
    }

    MESAS {
        int id PK
        int numero
        int capacidad
        enum estado
    }

    CATEGORIAS {
        int id PK
        varchar nombre
        varchar descripcion
    }

    PRODUCTOS {
        int id PK
        varchar nombre
        varchar descripcion
        decimal precio
        boolean disponible
        int categoria_id FK
    }

    PEDIDOS {
        int id PK
        enum tipo
        enum estado
        text observaciones
        decimal total
        int mesa_id FK
        int usuario_id FK
        int cliente_id FK
        datetime created_at
        datetime updated_at
    }

    DETALLE_PEDIDOS {
        int id PK
        int pedido_id FK
        int producto_id FK
        int cantidad
        decimal precio_unit
        decimal subtotal
        varchar nota
    }

    CLIENTES {
        int id PK
        varchar nombre
        varchar telefono
        varchar direccion
        varchar barrio
        varchar referencia
        datetime created_at
    }

    DOMICILIOS {
        int id PK
        int pedido_id FK
        varchar direccion_entrega
        varchar barrio
        decimal costo_envio
        enum estado
        datetime fecha_hora_entrega
    }

    PAGOS {
        int id PK
        int pedido_id FK
        decimal monto
        enum tipo_pago
        enum estado_pago
        varchar referencia
        datetime fecha_hora
    }