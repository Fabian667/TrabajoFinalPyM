# Checklist de Cumplimiento con la Guía del Trabajo Final

---

## 1. Definición del Problema y Nicho ✅
- **Descripción del nicho**: PyMEs de fabricación de muebles de madera
- **Dolores identificados**:
  - Control de inventario deficiente
  - Seguimiento manual de órdenes de producción
  - Poca visibilidad de costos
  - Sin integración con ecommerce
- **Documentación**: [01-nicho-mercado.md](./01-nicho-mercado.md)

---

## 2. Análisis de Requisitos ✅
- **Entrevistas con clientes**: Guía completa estructurada
- **Preguntas por perfil**: Propietario, Jefe de Producción, Jefe de Ventas
- **Documentación**:
  - [02-entrevistas-clientes.md](./02-entrevistas-clientes.md)
  - [05-entrevistas-completas.md](./05-entrevistas-completas.md)

---

## 3. Modelado del Sistema ✅
- **Modelo Entidad-Relación (ER) de BD**: 15 entidades principales con relaciones
- **Diagramas UML de clases**: Todas las entidades del dominio con atributos y métodos
- **Documentación**:
  - [03-modelo-er.md](./03-modelo-er.md)
  - [04-uml-clases.md](./04-uml-clases.md)

---

## 4. Diseño de la Arquitectura ✅
- **Arquitectura**: Cliente-Servidor (API REST)
- **Backend**: Spring Boot 3.2 (Java 17)
- **Frontend**: Angular 17
- **Estructura de proyectos**:
  - `erp-backend/`: Repositorios, servicios, controladores
  - `erp-frontend/`: Configuración inicial y componentes base
- **Tecnologías validadas**: Alineadas con estándares industriales

---

## 5. Implementación (Esqueleto) ✅
- **Backend**:
  - Entidades JPA completas (15 entidades)
  - Repositorios Spring Data JPA
  - Servicios y controladores base (ej: ProductService, ProductController)
  - Configuración de BD (H2 para desarrollo, MySQL para producción)
- **Frontend**:
  - Configuración inicial de Angular
  - Rutas base
  - HttpClient configurado

---

## 6. Integración con Ecommerce ✅
- **Diseñado en el modelo**: Campo `isEcommerce` en la entidad `Order` para diferenciar pedidos online vs. offline
- **Listo para integrar**: Estructura preparada para conectar con plataformas como Shopify, WooCommerce o un frontend propio

---

## 7. Plan de Deploy ✅
- **Recomendaciones de servidores**: Low cost (~ $12/mes total)
- **Pasos detallados**: Para backend, frontend y BD
- **Documentación**: [06-recomendaciones-servidores.md](./06-recomendaciones-servidores.md)

---

## Próximos Pasos (Si la Guía Lo Requiere)
Si la guía pide más detalles, podemos agregar:
1. **Wireframes/Pantallas**: Diseños de la interfaz de usuario
2. **Casos de Uso**: Diagramas UML de casos de uso
3. **Pruebas**: Plan de pruebas unitarias y de integración
4. **Presupuesto**: Detalle de costos de desarrollo y mantenimiento
5. **Manual de Usuario**: Guía para usar el ERP

---

## Preguntas para Validar con la Guía
¿La guía del trabajo final pide alguno de estos elementos adicionales?
- Abstract/Resumen ejecutivo
- Marco teórico
- Estado del arte (sistemas similares)
- Metodología de desarrollo (Scrum,瀑布, etc.)
- Presupuesto detallado
- Cronograma de trabajo
