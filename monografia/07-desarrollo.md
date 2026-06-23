# 7. Desarrollo y Análisis

---

## 7.1. Definición del nicho de mercado

El nicho elegido son las **PyMEs de fabricación de muebles de madera** (5 a 50 empleados), ya que:
- Tienen dolores claros y urgentes: control de inventario deficiente, seguimiento manual de órdenes
- Son numerosas y tienen potencial de adopción de tecnologías
- Necesitan integración con ecommerce para competir en el mercado actual

Los dolores principales identificados son:
1. Control de inventario de materias primas manual (hojas de cálculo o papel)
2. Seguimiento de órdenes de producción sin visibilidad en tiempo real
3. Poca información sobre costos reales de fabricación
4. Sin conexión entre ventas online y procesos internos

## 7.2. Análisis del proceso productivo de muebles de madera

### 7.2.1. Diagrama de Operaciones del Proceso (DOP)

| Paso | Operación | Descripción | Tiempo estimado |
|------|-----------|-------------|-----------------|
| 1 | Recepcionar MP | Recepción de materias primas (madera, herrajes, pintura) | 15 min |
| 2 | Almacenar MP | Almacenamiento en depósito de materias primas | 10 min |
| 3 | Cortar madera | Corte y dimensionado de piezas de madera | 30 min |
| 4 | Mecanizar | Perforación, rebajado, moldeado | 25 min |
| 5 | Ensamblar | Unión de piezas para formar la estructura | 40 min |
| 6 | Lijar | Preparación de la superficie para acabado | 20 min |
| 7 | Acabar | Pintura o barnizado | 45 min + secado |
| 8 | Controlar calidad | Verificación de especificaciones | 10 min |
| 9 | Embalar | Empaque para envío o venta | 15 min |
| 10 | Almacenar PT | Almacenamiento en depósito de productos terminados | 10 min |

*(Nota: El diagrama gráfico DOP/DAP se incluirá en el Anexo B)*

### 7.2.2. Diagrama de Análisis del Proceso (DAP)

| Paso | Tipo | Actividad | Tiempo | Distancia | Observaciones |
|------|------|-----------|--------|-----------|---------------|
| 1 | O | Recepcionar MP | 15' | - | |
| 2 | T | Trasladar a depósito | - | 20 m | |
| 3 | A | Almacenar MP | 10' | - | |
| 4 | T | Trasladar a taller | - | 30 m | |
| 5 | O | Cortar madera | 30' | - | |
| 6 | I | Inspección parcial | 5' | - | Oportunidad de mejora |
| 7 | O | Mecanizar | 25' | - | |
| 8 | O | Ensamblar | 40' | - | |
| 9 | O | Lijar | 20' | - | |
| 10 | O | Acabar | 45' | - | |
| 11 | D | Secado | 120' | - | |
| 12 | I | Control de calidad final | 10' | - | |
| 13 | O | Embalar | 15' | - | |
| 14 | T | Trasladar a depósito PT | - | 25 m | |
| 15 | A | Almacenar PT | 10' | - | |

### 7.2.3. Oportunidades de mejora identificadas

1. **Control de inventario**: Implementar un sistema digital para seguimiento de MP y PT
2. **Seguimiento de órdenes**: Registrar el avance de cada orden en el ERP para visibilidad en tiempo real
3. **Reducción de tiempos de traslado**: Optimizar la disposición física del taller
4. **Integración con ecommerce**: Sincronizar inventario PT con la tienda online

## 7.3. Modelado del sistema ERP

### 7.3.1. Modelo Entidad-Relación (ER)

El modelo ER incluye 15 entidades principales:
- `Category` (categorías de productos)
- `Product` (productos terminados)
- `RawMaterial` (materias primas)
- `Supplier` (proveedores)
- `ProductionOrder` (órdenes de producción)
- `ProductionStage` (etapas de producción)
- `StageLog` (registros de etapas)
- `MaterialConsumption` (consumo de MP)
- `BillOfMaterials` (lista de materiales)
- `Customer` (clientes)
- `Order` (pedidos de clientes, con flag `isEcommerce`)
- `OrderItem` (items del pedido)
- `User` (usuarios del sistema)
- `PurchaseOrder` (órdenes de compra)
- `PurchaseItem` (items de compra)

*(El diagrama ER gráfico se incluye en el Anexo B y en la carpeta docs/03-modelo-er.md)*

### 7.3.2. Diagramas UML de clases

Se diseñaron diagramas UML de clases para todas las entidades del dominio, con atributos, métodos y relaciones. Destacan:
- `ProductionOrder` con relación a `Product`, `StageLog` y `MaterialConsumption`
- `Order` con relación a `Customer` y `OrderItem`, y atributo `isEcommerce` para diferenciar pedidos online
- `User` con atributo `role` para control de acceso (ADMIN, PRODUCCION, VENTAS, ALMACEN)

*(Los diagramas UML completos están en docs/04-uml-clases.md)*

## 7.4. Diseño de la arquitectura técnica

### 7.4.1. Backend con Spring Boot

El backend se desarrolló con **Spring Boot 3.2** (Java 17), con la siguiente estructura:
- `entity/`: Entidades JPA mapeadas a la BD
- `repository/`: Repositorios Spring Data JPA
- `service/`: Servicios de negocio
- `controller/`: Controladores REST API
- `security/`: Autenticación y autorización (JWT)

Base de datos:
- H2 para desarrollo (en memoria)
- MySQL para producción

### 7.4.2. Frontend con Angular

El frontend se desarrolló con **Angular 17**, con:
- Componentes standalone
- Rutas para navegación
- Servicios para consumo de la API REST
- Interfaz de usuario adaptada a equipos no técnicos

## 7.5. Integración con ecommerce

El sistema está preparado para:
1. **Sincronización de inventario**: El campo `stock` de `Product` se actualiza automáticamente y se envía al ecommerce.
2. **Flujo de pedidos online**: Cuando un cliente compra en el ecommerce, se crea un `Order` en el ERP con `isEcommerce = true`.
3. **Visibilidad para clientes**: Los clientes pueden ver el estado de su pedido en tiempo real.
4. **Actualización de estado**: Cuando la orden de producción se completa, el estado del pedido online se actualiza automáticamente.

## 7.6. Aplicación de IA e Industria 4.0

Se proponen las siguientes aplicaciones:
1. **Mantenimiento predictivo**: Algoritmos de ML para predecir fallos en máquinas de corte y lijado, basados en datos de vibración y temperatura.
2. **Optimización de inventario**: IA para predecir demanda de materias primas y calcular puntos de pedido automáticos.
3. **Control de calidad por visión artificial**: Cámaras en la estación de pintura para detectar defectos de acabado.
4. **Planificación automática**: IA para priorizar órdenes de producción según fechas de entrega y disponibilidad de MP.
