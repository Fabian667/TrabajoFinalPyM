# 🚀 Generar la Monografía en Google Colab (SIN INSTALAR NADA!)

Google Colab es una herramienta gratuita de Google que te permite ejecutar código Python directamente en el navegador—sin instalar nada en tu máquina.

---

## 📝 Paso 1: Abrir Google Colab
1. Ve a https://colab.research.google.com/
2. Haz clic en **"Nuevo cuaderno"** (New notebook)

---

## 📝 Paso 2: Instalar la librería
En la primera celda (celda de código) que aparece, escribe y ejecuta (Shift + Enter):
```python
!pip install python-docx
```

---

## 📝 Paso 3: Pegar el script
Crea una **nueva celda** (botón "+ Código" en la barra superior) y pega TODO el contenido del archivo `generar-monografia-word.py`.

---

## 📝 Paso 4: Ejecutar el script
Haz clic en el botón de **"Play"** (▶️) en la celda del script. Espera unos segundos—listo!

---

## 📝 Paso 5: Descargar el archivo Word
Agrega **una última celda** con este código para descargar el archivo:
```python
from google.colab import files
files.download('Monografia-Trabajo-Final.docx')
```

Ejecuta esta celda y el archivo se descargará automáticamente a tu computadora!

---

## ✅ ¡Listo!
Ahora tienes tu monografía completa en formato Word. Solo falta:
1. Llenar los espacios en blanco (nombres, grupo, fecha)
2. Agregar las imágenes de los diagramas (DOP, DAP, ER, UML)
3. Actualizar el índice
