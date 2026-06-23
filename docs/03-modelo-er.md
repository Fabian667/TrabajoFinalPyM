# Modelo Entidad-Relación (ER) - ERP para Fabricación de Muebles

## Entidades Principales

### 1. Categoría (category)
- id (PK)
- nombre
- descripción

### 2. Producto (product)
- id (PK)
- nombre
- descripción
- precio
- stock
- category_id (FK)
- sku
- imagen_url

### 3. Materia Prima (raw_material)
- id (PK)
- nombre
- descripción
- unidad_medida (kg, m, unidades)
- stock
- costo_unitario
- proveedor_id (FK)

### 4. Proveedor (supplier)
- id (PK)
- nombre
- contacto
- email
- teléfono
- dirección

### 5. Orden de Producción (production_order)
- id (PK)
- numero
- fecha_creacion
- fecha_inicio
- fecha_fin
- estado (PENDIENTE, EN_PRODUCCION, TERMINADA, CANCELADA)
- product_id (FK)
- cantidad
- observaciones

### 6. Etapa de Producción (production_stage)
- id (PK)
- nombre (Corte, Ensamblado, Lijado, Pintura, Empaque)
- orden
- descripción

### 7. Registro de Etapa (stage_log)
- id (PK)
- production_order_id (FK)
- production_stage_id (FK)
- fecha_inicio
- fecha_fin
- usuario_id (FK)
- observaciones

### 8. Consumo de Materia Prima (material_consumption)
- id (PK)
- production_order_id (FK)
- raw_material_id (FK)
- cantidad_consumida

### 9. Lista de Materiales (bill_of_materials)
- id (PK)
- product_id (FK)
- raw_material_id (FK)
- cantidad_necesaria

### 10. Cliente (customer)
- id (PK)
- nombre
- email
- teléfono
- dirección

### 11. Pedido (order)
- id (PK)
- numero
- fecha
- total
- estado (PENDIENTE, PAGADO, ENVIADO, ENTREGADO, CANCELADO)
- customer_id (FK)
- es_ecommerce (boolean)

### 12. Detalle de Pedido (order_item)
- id (PK)
- order_id (FK)
- product_id (FK)
- cantidad
- precio_unitario

### 13. Usuario (user)
- id (PK)
- nombre
- email
- password_hash
- rol (ADMIN, PRODUCCION, VENTAS, ALMACEN)

### 14. Compra de Materia Prima (purchase_order)
- id (PK)
- numero
- fecha
- total
- estado (PENDIENTE, RECIBIDA, CANCELADA)
- supplier_id (FK)

### 15. Detalle de Compra (purchase_item)
- id (PK)
- purchase_order_id (FK)
- raw_material_id (FK)
- cantidad
- precio_unitario

## Relaciones
- Producto → Categoría (N:1)
- Producto → Lista de Materiales → Materia Prima (N:M)
- Orden de Producción → Producto (N:1)
- Orden de Producción → Registros de Etapa → Etapa de Producción (N:M)
- Orden de Producción → Consumo de Materia Prima → Materia Prima (N:M)
- Pedido → Cliente (N:1)
- Pedido → Detalle de Pedido → Producto (N:M)
- Compra → Proveedor (N:1)
- Compra → Detalle de Compra → Materia Prima (N:M)
