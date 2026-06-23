# Recomendaciones de Servidores para Deploy del ERP

---

## 1. Backend (Spring Boot)

### Opción A: Cloud (Recomendado para empezar)
- **Render** (render.com)
  - Precio: Plan Starter ~ $7/mes
  - Ventajas: Fácil de deployar, SSL incluido, auto-scaling básico
  - Compatible con Java/Spring Boot
- **Railway** (railway.app)
  - Precio: Plan Starter ~ $5/mes
  - Ventajas: Muy intuitivo, integración con GitHub
- **Heroku** (heroku.com)
  - Precio: Hobby ~ $7/mes
  - Ventajas: Ecosistema maduro, muchos add-ons

### Opción B: VPS (Mayor control)
- **DigitalOcean** (digitalocean.com)
  - Droplet básico (1GB RAM, 1 CPU): ~ $6/mes
  - Ventajas: Precio accesible, buena documentación
- **Vultr** (vultr.com)
  - Plan similar: ~ $5/mes
- **AWS EC2** (aws.amazon.com)
  - Free Tier disponible por 12 meses
  - Ventajas: Escalable, pero mayor complejidad

---

## 2. Frontend (Angular)

### Opción A: Hosting Static (Recomendado)
- **Vercel** (vercel.com)
  - Precio: Gratis para proyectos pequeños
  - Ventajas: Muy rápido, integración con GitHub, SSL
- **Netlify** (netlify.com)
  - Precio: Gratis para proyectos pequeños
  - Ventajas: Fácil de usar, CI/CD automático
- **GitHub Pages** (pages.github.com)
  - Precio: Gratis
  - Ventajas: Ideal si el código está en GitHub

---

## 3. Base de Datos

### Opción A: Cloud (Recomendado)
- **PostgreSQL en Render/Railway**: Incluido en planes o ~ $7/mes adicional
- **AWS RDS**: Free Tier disponible
- **Supabase**: Gratis para uso moderado
- **PlanetScale**: MySQL compatible, gratis para empezar

### Opción B: Mismo servidor que backend
- PostgreSQL/MySQL instalado en el mismo VPS (ahorra costos)

---

## 4. Recomendación Inicial (Low Cost)

### Stack Completo ~ $12/mes
1. **Backend**: Render Starter ($7)
2. **Frontend**: Vercel (Gratis)
3. **BD**: PostgreSQL en Render ($5 adicional o usar BD incluida)

### Ventajas
- Bajo costo inicial
- Fácil de configurar
- Escalable a medida que crece el negocio

---

## 5. Pasos para Deploy

### Backend Spring Boot
1. Generar JAR: `mvn clean package`
2. Subir a Render/Railway
3. Configurar variables de entorno (BD, JWT secret, etc.)
4. Listo!

### Frontend Angular
1. Build para producción: `ng build --configuration production`
2. Subir carpeta `dist/` a Vercel/Netlify
3. Configurar dominio (opcional)
4. Listo!
