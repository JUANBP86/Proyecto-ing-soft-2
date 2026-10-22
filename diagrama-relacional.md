# Diagrama relacional del proyecto

```mermaid
erDiagram
    CLIENTES ||--o{ PEDIDOS : realiza
    MESEROS ||--o{ PEDIDOS : atiende
    COCINAS ||--o{ PEDIDOS : prepara
    ADMINISTRADORES ||--o{ PEDIDOS : supervisa
    PEDIDOS ||--o{ DETALLE_PEDIDOS : incluye
    PRODUCTOS ||--o{ DETALLE_PEDIDOS : aparece_en
    CATEGORIAS ||--o{ PRODUCTOS : contiene
    PEDIDOS ||--o| DOMICILIOS : tiene
    PEDIDOS ||--o| PAGOS : registra
    PEDIDOS ||--o{ PEDIDO_MESA : incluye
    MESAS ||--o{ PEDIDO_MESA : participa_en

    CLIENTES {
        int id PK
        varchar nombre
        varchar telefono
        varchar direccion
        varchar email
        datetime created_at
    }

    MESEROS {
        int id PK
        varchar nombre
        varchar dni
        varchar telefono
        varchar email
        datetime created_at
    }

    COCINAS {
        int id PK
        varchar nombre
        varchar dni
        varchar telefono
        varchar email
        datetime created_at
    }

    ADMINISTRADORES {
        int id PK
        varchar nombre
        varchar dni
        varchar email
        varchar password
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
        int cliente_id FK
        int mesero_id FK
        int cocina_id FK
        int administrador_id FK
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

    PEDIDO_MESA {
        int id PK
        int pedido_id FK
        int mesa_id FK
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
```

## Cómo editarlo

1. Abre este archivo en VS Code.
2. Haz clic en la vista previa Markdown (Ctrl + Shift + V).
3. Si quieres cambiar algo, edita el bloque Mermaid directamente.
4. Puedes volver a abrir la vista previa para ver el resultado.

> Esto permite que lo puedas modificar antes de mostrárselo al profesor sin perder la visualización del diagrama.
