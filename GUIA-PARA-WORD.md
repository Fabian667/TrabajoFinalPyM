# 📝 Guía para convertir la monografía a formato Word

---

## 🚀 Método 1: Usar el script Python (RECOMENDADO - AUTOMÁTICO!)

Esta es la forma más fácil y rápida: ¡el script genera el Word con todo el formato listo!

### Paso 1: Instalar Python (si no lo tienes)
1. Ve a https://www.python.org/downloads/
2. Descarga la última versión de Python (3.9 o superior)
3. Instálalo, y asegúrate de marcar la opción **"Add Python to PATH"**

### Paso 2: Instalar la librería necesaria
Abre una terminal (CMD o PowerShell en Windows, Terminal en Mac/Linux) y ejecuta:
```bash
pip install python-docx
```
o si tienes el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecutar el script
En la terminal, navega hasta la carpeta del proyecto y ejecuta:
```bash
python generar-monografia-word.py
```
*(Nota: En Windows, si `python` no funciona, prueba con `py`)*

### Paso 4: ¡Listo!
Se generará automáticamente el archivo **`Monografia-Trabajo-Final.docx`** con todo el formato:
- Portada, índice, todas las secciones
- Fuente Arial 12
- Interlineado 1.5
- Márgenes correctos
- Listas con viñetas
- Títulos con niveles

---

## Método 2: Usar Google Docs (si prefieres no usar Python)

### Paso 1: Crear un nuevo documento en Google Docs
1. Ve a https://docs.google.com
2. Haz clic en **Blank** para crear un documento nuevo.

### Paso 2: Copiar y pegar todas las secciones
Abre cada archivo `.md` de la carpeta `monografia/` y copia todo el contenido, luego pégalo en Google Docs en este orden:
1. `01-portada.md`
2. `02-indice.md`
3. `03-resumen.md`
4. `04-introduccion.md`
5. `05-marco-teorico.md`
6. `06-metodologia.md`
7. `07-desarrollo.md`
8. `08-conclusiones.md`
9. `09-referencias.md`
10. `10-anexo-a.md`
11. `11-anexo-b.md`

### Paso 3: Dar formato al documento
- **Fuente**: Selecciona todo el texto y elige **Arial** o **Calibri**, tamaño **11 o 12**
- **Interlineado**: Elige **1.5** o **Doble**
- **Márgenes**: Ve a `Archivo > Configurar página` y configura márgenes normales (2.5 cm aprox.)
- **Encabezados y títulos**: Usa los estilos de Google Docs ("Título 1", "Título 2", etc.) para que el índice sea navegable

### Paso 4: Exportar a Word
1. En Google Docs, ve a `Archivo > Descargar > Microsoft Word (.docx)`
2. ¡Listo!

---

## Método 3: Usar Microsoft Word directamente

1. Abre Microsoft Word y crea un documento nuevo
2. Copia y pega cada sección como en el método 2
3. Usa las herramientas de formato de Word para darle estilo.

---

## ✅ Lista de verificación final para la entrega

Antes de entregar, asegúrate de:
1. Haber completado todos los espacios en blanco en el documento Word:
   - Nombres de integrantes del grupo
   - Número de grupo
   - Nombre del profesor
   - Nombre de la universidad/materia
   - Fecha de entrega
2. Haber agregado las imágenes de los diagramas (DOP, DAP, ER, UML) en el Anexo B
3. Haber actualizado los números de página en el índice
4. Haber revisado la redacción y la ortografía
5. Haber guardado el archivo con el nombre: `TF_Grupo-NN.docx` (donde NN es el número de grupo)


