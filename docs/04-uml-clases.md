# Diagramas UML de Clases - ERP para Fabricación de Muebles

## Clases del Dominio

### 1. Category
```
+---------------------+
| Category            |
+---------------------+
| - id: Long          |
| - name: String      |
| - description: String|
+---------------------+
| + getId(): Long     |
| + getName(): String |
| + getProducts(): List<Product> |
+---------------------+
```

### 2. Product
```
+---------------------------+
| Product                   |
+---------------------------+
| - id: Long                |
| - name: String            |
| - description: String     |
| - price: BigDecimal       |
| - stock: Integer          |
| - sku: String             |
| - imageUrl: String        |
| - category: Category      |
+---------------------------+
| + getId(): Long           |
| + getPrice(): BigDecimal  |
| + getBillOfMaterials(): List<BillOfMaterials> |
+---------------------------+
```

### 3. RawMaterial
```
+------------------------------+
| RawMaterial                  |
+------------------------------+
| - id: Long                   |
| - name: String               |
| - description: String        |
| - unit: String               |
| - stock: BigDecimal          |
| - unitCost: BigDecimal       |
| - supplier: Supplier         |
+------------------------------+
| + getId(): Long              |
| + getUnitCost(): BigDecimal  |
+------------------------------+
```

### 4. Supplier
```
+------------------------+
| Supplier               |
+------------------------+
| - id: Long             |
| - name: String         |
| - contact: String      |
| - email: String        |
| - phone: String        |
| - address: String      |
+------------------------+
| + getId(): Long        |
| + getPurchaseOrders(): List<PurchaseOrder> |
+------------------------+
```

### 5. ProductionOrder
```
+-----------------------------------+
| ProductionOrder                   |
+-----------------------------------+
| - id: Long                        |
| - number: String                  |
| - creationDate: LocalDate         |
| - startDate: LocalDate            |
| - endDate: LocalDate              |
| - status: ProductionOrderStatus   |
| - product: Product                |
| - quantity: Integer               |
| - observations: String            |
+-----------------------------------+
| + getId(): Long                   |
| + getStatus(): ProductionOrderStatus |
| + getStageLogs(): List<StageLog>  |
| + getMaterialConsumptions(): List<MaterialConsumption> |
+-----------------------------------+
```

### 6. ProductionStage
```
+------------------------------+
| ProductionStage              |
+------------------------------+
| - id: Long                   |
| - name: String               |
| - order: Integer             |
| - description: String        |
+------------------------------+
| + getId(): Long              |
| + getName(): String          |
+------------------------------+
```

### 7. StageLog
```
+----------------------------------+
| StageLog                         |
+----------------------------------+
| - id: Long                       |
| - productionOrder: ProductionOrder |
| - stage: ProductionStage         |
| - startDate: LocalDateTime       |
| - endDate: LocalDateTime         |
| - user: User                     |
| - observations: String           |
+----------------------------------+
| + getId(): Long                  |
+----------------------------------+
```

### 8. MaterialConsumption
```
+----------------------------------+
| MaterialConsumption              |
+----------------------------------+
| - id: Long                       |
| - productionOrder: ProductionOrder |
| - rawMaterial: RawMaterial       |
| - quantity: BigDecimal           |
+----------------------------------+
| + getId(): Long                  |
+----------------------------------+
```

### 9. BillOfMaterials
```
+----------------------------------+
| BillOfMaterials                  |
+----------------------------------+
| - id: Long                       |
| - product: Product               |
| - rawMaterial: RawMaterial       |
| - requiredQuantity: BigDecimal   |
+----------------------------------+
| + getId(): Long                  |
+----------------------------------+
```

### 10. Customer
```
+------------------------+
| Customer               |
+------------------------+
| - id: Long             |
| - name: String         |
| - email: String        |
| - phone: String        |
| - address: String      |
+------------------------+
| + getId(): Long        |
| + getOrders(): List<Order> |
+------------------------+
```

### 11. Order
```
+----------------------------------+
| Order                            |
+----------------------------------+
| - id: Long                       |
| - number: String                 |
| - date: LocalDate                |
| - total: BigDecimal              |
| - status: OrderStatus            |
| - customer: Customer             |
| - isEcommerce: Boolean           |
+----------------------------------+
| + getId(): Long                  |
| + getTotal(): BigDecimal         |
| + getOrderItems(): List<OrderItem> |
+----------------------------------+
```

### 12. OrderItem
```
+----------------------------------+
| OrderItem                        |
+----------------------------------+
| - id: Long                       |
| - order: Order                   |
| - product: Product               |
| - quantity: Integer              |
| - unitPrice: BigDecimal          |
+----------------------------------+
| + getId(): Long                  |
| + getSubtotal(): BigDecimal      |
+----------------------------------+
```

### 13. User
```
+----------------------------------+
| User                             |
+----------------------------------+
| - id: Long                       |
| - name: String                   |
| - email: String                  |
| - passwordHash: String           |
| - role: UserRole                 |
+----------------------------------+
| + getId(): Long                  |
| + getRole(): UserRole            |
+----------------------------------+
```

### 14. PurchaseOrder
```
+----------------------------------+
| PurchaseOrder                    |
+----------------------------------+
| - id: Long                       |
| - number: String                 |
| - date: LocalDate                |
| - total: BigDecimal              |
| - status: PurchaseOrderStatus    |
| - supplier: Supplier             |
+----------------------------------+
| + getId(): Long                  |
| + getPurchaseItems(): List<PurchaseItem> |
+----------------------------------+
```

### 15. PurchaseItem
```
+----------------------------------+
| PurchaseItem                     |
+----------------------------------+
| - id: Long                       |
| - purchaseOrder: PurchaseOrder   |
| - rawMaterial: RawMaterial       |
| - quantity: BigDecimal           |
| - unitPrice: BigDecimal          |
+----------------------------------+
| + getId(): Long                  |
+----------------------------------+
```

## Enumeraciones

### ProductionOrderStatus
- PENDIENTE
- EN_PRODUCCION
- TERMINADA
- CANCELADA

### OrderStatus
- PENDIENTE
- PAGADO
- ENVIADO
- ENTREGADO
- CANCELADO

### PurchaseOrderStatus
- PENDIENTE
- RECIBIDA
- CANCELADA

### UserRole
- ADMIN
- PRODUCCION
- VENTAS
- ALMACEN
