## 10.2. Anexo B — Material de apoyo

---

### B.1. Diagrama de Operaciones del Proceso (DOP) — Versión gráfica

*(Nota: El diagrama gráfico DOP se deberá crear con herramientas como Draw.io, Lucidchart o similar y agregar en esta sección. Se incluye una representación textual en la sección 7.2.1 de la monografía)*

### B.2. Diagrama de Análisis del Proceso (DAP) — Versión gráfica

*(Nota: El diagrama gráfico DAP se deberá crear con herramientas como Draw.io, Lucidchart o similar y agregar en esta sección. Se incluye una representación textual en la sección 7.2.2 de la monografía)*

### B.3. Modelo Entidad-Relación (ER) — Versión gráfica

*(Nota: El diagrama ER gráfico se encuentra en la carpeta docs/03-modelo-er.md y se deberá exportar como imagen y agregar aquí)*

### B.4. Diagramas UML de clases — Versión gráfica

*(Nota: Los diagramas UML completos se encuentran en la carpeta docs/04-uml-clases.md y se deberán exportar como imágenes y agregar aquí)*

### B.5. Estructura del proyecto Spring Boot (listado de archivos)

```
erp-backend/
├── pom.xml
└── src/
    └── main/
        ├── java/com/erpmuebles/erp/
        │   ├── ErpApplication.java
        │   ├── entity/
        │   │   ├── Category.java
        │   │   ├── Product.java
        │   │   ├── RawMaterial.java
        │   │   ├── Supplier.java
        │   │   ├── ProductionOrder.java
        │   │   ├── ProductionStage.java
        │   │   ├── StageLog.java
        │   │   ├── MaterialConsumption.java
        │   │   ├── BillOfMaterials.java
        │   │   ├── Customer.java
        │   │   ├── Order.java
        │   │   ├── OrderItem.java
        │   │   ├── User.java
        │   │   ├── PurchaseOrder.java
        │   │   └── PurchaseItem.java
        │   ├── repository/
        │   ├── service/
        │   ├── controller/
        │   ├── dto/
        │   ├── config/
        │   └── security/
        └── resources/
            └── application.properties
```

### B.6. Estructura del proyecto Angular (listado de archivos)

```
erp-frontend/
├── package.json
├── angular.json
└── src/
    ├── index.html
    ├── main.ts
    ├── styles.css
    └── app/
        ├── app.component.ts
        ├── app.config.ts
        └── app.routes.ts
```

### B.7. Guía de entrevistas con clientes potenciales

*(Nota: La guía completa se encuentra en la carpeta docs/02-entrevistas-clientes.md y docs/05-entrevistas-completas.md)*

### B.8. Plan de deploy del sistema

*(Nota: El plan completo se encuentra en la carpeta docs/06-recomendaciones-servidores.md)*
