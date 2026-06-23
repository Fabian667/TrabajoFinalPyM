#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar la monografía del trabajo final en formato Word (.docx)
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import os


def set_font(paragraph, font_name="Arial", size=12, bold=False):
    """Configurar la fuente de un párrafo"""
    run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
    font = run.font
    font.name = font_name
    font.size = Pt(size)
    font.bold = bold
    # Establecer fuente para texto en español también
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    return run


def add_title(doc, text, level=1):
    """Agregar un título con formato"""
    para = doc.add_heading(text, level=level)
    set_font(para, "Arial", size=14 + (2 - level), bold=True)
    return para


def add_paragraph(doc, text, font_name="Arial", size=12):
    """Agregar un párrafo con formato"""
    para = doc.add_paragraph(text)
    para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    para.paragraph_format.line_spacing = 1.5
    para.paragraph_format.space_after = Pt(6)
    if para.runs:
        set_font(para, font_name, size)
    return para


def add_list_item(doc, text, font_name="Arial", size=12):
    """Agregar un elemento de lista"""
    para = doc.add_paragraph(text, style='List Bullet')
    para.paragraph_format.line_spacing = 1.5
    para.paragraph_format.space_after = Pt(3)
    if para.runs:
        set_font(para, font_name, size)
    return para


def main():
    print("📝 Generando monografía en formato Word...")

    # Crear documento
    doc = Document()

    # Configurar márgenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.2)
        section.right_margin = Inches(1.2)

    # --------------------------
    # 1. Portada
    # --------------------------
    add_title(doc, "1. Portada", level=1)

    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run("ERP para Procesos Productivos de Muebles de Madera\n")
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.name = "Arial"
    run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')

    para.add_run("\nTrabajo Final Integrador\nMateria: Producción y Materiales\nEdición 2026\n\n").font.size = Pt(14)

    run = para.add_run("Integrantes del grupo:\n")
    run.font.size = Pt(12)
    run.font.bold = True

    run = para.add_run("[Integrante 1]\n[Integrante 2]\n[Integrante 3]\n[Integrante 4]\n[Integrante 5]\n\n")
    run.font.size = Pt(12)

    run = para.add_run("Número de grupo: [NN]\nProfesor: Lic. Ignacio Joaquín\n\nFecha de entrega: [DD/MM/2026]")
    run.font.size = Pt(12)

    doc.add_page_break()

    # --------------------------
    # 2. Índice
    # --------------------------
    add_title(doc, "2. Índice", level=1)

    index_items = [
        "1. Portada",
        "2. Índice",
        "3. Resumen",
        "4. Introducción",
        "   4.1. Presentación del tema e importancia",
        "   4.2. Problemática (externa)",
        "   4.3. Necesidad (interna)",
        "   4.4. Oportunidad (interna o externa)",
        "   4.5. Objetivos",
        "       4.5.1. Objetivo general",
        "       4.5.2. Objetivos específicos",
        "   4.6. Metodología",
        "5. Marco teórico",
        "   5.1. Procesos productivos en la fabricación de muebles",
        "   5.2. Gestión de inventario de materias primas y productos terminados",
        "   5.3. Integración de sistemas ERP con ecommerce",
        "   5.4. Industria 4.0 y aplicación de IA en procesos productivos",
        "6. Metodología",
        "   6.1. Enfoque de investigación",
        "   6.2. Métodos de recolección de datos",
        "7. Desarrollo y Análisis",
        "   7.1. Definición del nicho de mercado",
        "   7.2. Análisis del proceso productivo de muebles de madera",
        "       7.2.1. Diagrama de Operaciones del Proceso (DOP)",
        "       7.2.2. Diagrama de Análisis del Proceso (DAP)",
        "   7.3. Modelado del sistema ERP",
        "       7.3.1. Modelo Entidad-Relación (ER)",
        "       7.3.2. Diagramas UML de clases",
        "   7.4. Diseño de la arquitectura técnica",
        "       7.4.1. Backend con Spring Boot",
        "       7.4.2. Frontend con Angular",
        "   7.5. Integración con ecommerce",
        "8. Conclusiones",
        "9. Referencias",
        "10. Anexos",
        "   10.1. Anexo A — Declaración de uso de Inteligencia Artificial",
        "   10.2. Anexo B — Material de apoyo",
    ]

    for item in index_items:
        add_paragraph(doc, item)

    doc.add_page_break()

    # --------------------------
    # 3. Resumen
    # --------------------------
    add_title(doc, "3. Resumen", level=1)

    add_paragraph(doc, "Este trabajo final presenta el diseño y desarrollo de un Sistema de Planificación de Recursos Empresariales (ERP) orientado a pequeñas y medianas empresas (PyMEs) de fabricación de muebles de madera, con integración nativa de ecommerce.")
    add_paragraph(doc, "El proyecto surge como respuesta a dolores comunes en este nicho: control de inventario deficiente, seguimiento manual de órdenes de producción, poca visibilidad de costos reales y falta de conexión entre procesos internos y ventas online.")
    add_paragraph(doc, "Se aplicaron conocimientos de procesos productivos, gestión de materiales, modelado de bases de datos y arquitectura de sistemas de información. Se desarrollaron diagramas DOP/DAP para el análisis del proceso de fabricación, un modelo Entidad-Relación (ER) para la base de datos, y diagramas UML de clases para el diseño del sistema.")
    add_paragraph(doc, "La arquitectura técnica se basa en Spring Boot para el backend (API REST) y Angular para el frontend, con una estructura escalable preparada para la integración con plataformas de ecommerce. Además, se incluye una propuesta de aplicación de Inteligencia Artificial en línea con la Industria 4.0 (mantenimiento predictivo, optimización de inventario, etc.).")
    add_paragraph(doc, "El trabajo demuestra cómo un ERP especializado puede mejorar la eficiencia operativa y la competitividad de PyMEs del sector mueblero, al integrar todos los procesos en un solo sistema y conectarlos con el canal de ventas online.")

    doc.add_page_break()

    # --------------------------
    # 4. Introducción
    # --------------------------
    add_title(doc, "4. Introducción", level=1)

    add_title(doc, "4.1. Presentación del tema e importancia", level=2)
    add_paragraph(doc, "La industria de fabricación de muebles de madera es un sector clave en la economía de muchos países, especialmente en el segmento de las pequeñas y medianas empresas (PyMEs). Sin embargo, muchas de estas empresas aún gestionan sus procesos de forma manual o con herramientas obsoletas, lo que genera ineficiencias, errores y pérdidas.")
    add_paragraph(doc, "El control de inventario de materias primas (madera, tornillos, pintura, etc.), el seguimiento de órdenes de producción y la conexión con las ventas son puntos críticos que, si no se gestionan bien, impactan directamente en la rentabilidad y la competitividad.")
    add_paragraph(doc, "Además, el auge del comercio electrónico ha transformado la forma en que los clientes compran muebles, y las PyMEs necesitan integrar sus procesos internos con sus canales de ventas online para no quedarse atrás.")

    add_title(doc, "4.2. Problemática (externa)", level=2)
    add_paragraph(doc, "Las PyMEs de fabricación de muebles de madera enfrentan una problemática externa relevante: la gestión ineficiente de sus procesos productivos y de inventario, lo que genera:")
    add_list_item(doc, "Provoca desabastecimiento de materias primas que detienen la producción")
    add_list_item(doc, "Genera sobrestock que incrementa costos de almacenamiento")
    add_list_item(doc, "Impide dar seguimiento en tiempo real a las órdenes de producción")
    add_list_item(doc, "No permite integrar las ventas por ecommerce con los procesos internos")
    add_list_item(doc, "Reduce la competitividad frente a empresas más grandes que sí usan sistemas integrados")

    add_title(doc, "4.3. Necesidad (interna)", level=2)
    add_paragraph(doc, "Este proyecto surge de una necesidad de la materia y de los equipos de trabajo: desarrollar un sistema que permita:")
    add_list_item(doc, "Controlar eficientemente el inventario de materias primas y productos terminados")
    add_list_item(doc, "Dar seguimiento a las órdenes de producción en tiempo real")
    add_list_item(doc, "Integrar los procesos internos con el canal de ecommerce")
    add_list_item(doc, "Proporcionar información para tomar decisiones basadas en datos")

    add_title(doc, "4.4. Oportunidad (interna o externa)", level=2)
    add_paragraph(doc, "Existe una oportunidad clara para:")
    add_list_item(doc, "Desarrollar un producto innovador: un ERP especializado y de bajo costo para PyMEs de muebles")
    add_list_item(doc, "Aplicar una nueva tecnología: integración de IA e Industria 4.0 en procesos productivos de PyMEs")
    add_list_item(doc, "Proveer a las organizaciones de un servicio que solucione sus dolores más urgentes")
    add_list_item(doc, "Responder a la demanda de las PyMEs por sistemas de gestión accesibles y fáciles de usar")

    add_title(doc, "4.5. Objetivos", level=2)
    add_title(doc, "4.5.1. Objetivo general", level=3)
    add_paragraph(doc, "Diseñar un sistema ERP especializado para PyMEs de fabricación de muebles de madera, que integre los procesos productivos, la gestión de materiales y las ventas por ecommerce.")

    add_title(doc, "4.5.2. Objetivos específicos", level=3)
    add_list_item(doc, "Analizar el proceso productivo de fabricación de muebles y sus materiales, elaborando diagramas DOP y DAP.")
    add_list_item(doc, "Definir los requisitos del sistema a partir del análisis de dolores del nicho.")
    add_list_item(doc, "Modelar la base de datos mediante un diagrama Entidad-Relación (ER).")
    add_list_item(doc, "Diseñar la arquitectura técnica del ERP usando diagramas UML de clases.")
    add_list_item(doc, "Proponer la integración del ERP con ecommerce.")
    add_list_item(doc, "Explorar aplicaciones de la Inteligencia Artificial en el proceso, en línea con la Industria 4.0.")
    add_list_item(doc, "Definir un plan de deploy del sistema en servidores cloud de bajo costo.")

    add_title(doc, "4.6. Metodología", level=2)
    add_paragraph(doc, "El trabajo se desarrolló mediante una investigación aplicada, con un enfoque cualitativo-cuantitativo. Se aplicaron métodos de recolección de datos como la investigación documental y el análisis de procesos y la elaboración de diagramas DOP y DAP para el análisis del proceso. También se usaron herramientas de Inteligencia Artificial para apoyo en la modelación y la estructuración del proyecto.")

    doc.add_page_break()

    # --------------------------
    # 5. Marco teórico
    # --------------------------
    add_title(doc, "5. Marco teórico", level=1)

    add_title(doc, "5.1. Procesos productivos en la fabricación de muebles", level=2)
    add_paragraph(doc, "Un proceso productivo es el conjunto de operaciones que transforman materias primas en productos terminados, agregando valor en cada etapa. Según Moscardo (2020), en la fabricación de muebles de madera, los procesos típicos son:")
    add_list_item(doc, "Recepción y almacenamiento de materias primas: Ingreso de madera, tableros, herrajes, pinturas, etc.")
    add_list_item(doc, "Corte y dimensionado: Corte de la madera a las medidas requeridas.")
    add_list_item(doc, "Mecanizado: Perforación, rebajado, moldeado de piezas.")
    add_list_item(doc, "Ensamblado: Unión de las piezas para formar la estructura del mueble.")
    add_list_item(doc, "Lijado: Preparación de la superficie para el acabado.")
    add_list_item(doc, "Acabado: Pintura, barnizado o revestimiento.")
    add_list_item(doc, "Control de calidad: Verificación de que el producto cumpla con las especificaciones.")
    add_list_item(doc, "Embalaje y almacenamiento de productos terminados: Preparación para la venta o envío.")

    add_title(doc, "5.2. Gestión de inventario de materias primas y productos terminados", level=2)
    add_paragraph(doc, "La gestión de inventario es fundamental para evitar desabastecimientos (que detienen la producción) y sobrestocks (que generan costos de almacenamiento y obsolescencia). Según Chase et al. (2021), los métodos más usados en PyMEs son:")
    add_list_item(doc, "ABC: Clasificación de items por valor (A: alto valor, bajo volumen; C: bajo valor, alto volumen)")
    add_list_item(doc, "EOQ (Economic Order Quantity): Cantidad óptima a pedir para minimizar costos totales")
    add_list_item(doc, "ROP (Reorder Point): Nivel de stock en el que se debe realizar un nuevo pedido")
    add_paragraph(doc, "En la fabricación de muebles, es crítico controlar: materias primas (madera, tableros, herrajes), productos en proceso (WIP - Work in Progress) y productos terminados.")

    add_title(doc, "5.3. Integración de sistemas ERP con ecommerce", level=2)
    add_paragraph(doc, "Un ERP (Enterprise Resource Planning) es un sistema que integra todos los procesos de una empresa en una sola plataforma: producción, compras, ventas, inventario, finanzas, etc. (Monk y Wagner, 2013).")
    add_paragraph(doc, "La integración de un ERP con ecommerce permite: sincronización automática de inventario entre la tienda online y el almacén, flujo directo de pedidos desde el ecommerce a la producción, visibilidad en tiempo real de la disponibilidad de productos para los clientes, cálculo preciso de costos y precios para el canal online.")

    add_title(doc, "5.4. Industria 4.0 y aplicación de IA en procesos productivos", level=2)
    add_paragraph(doc, "La Industria 4.0 es la cuarta revolución industrial, que combina tecnologías digitales, físicas y biológicas para transformar la manufactura. Según la Unidad 8 del programa de la materia, algunas aplicaciones relevantes para este proyecto son:")
    add_list_item(doc, "Mantenimiento predictivo: Uso de algoritmos de Machine Learning para predecir fallos en máquinas de producción (ej: sierras, lijadoras).")
    add_list_item(doc, "Optimización de inventario: IA para predecir la demanda de materias primas y productos terminados.")
    add_list_item(doc, "Control de calidad por visión artificial: Cámaras y algoritmos para detectar defectos en piezas de madera.")
    add_list_item(doc, "Gemelos digitales: Representación virtual del proceso productivo para simular cambios y optimizarlo.")
    add_list_item(doc, "Planificación automática de órdenes de producción: IA para asignar recursos y priorizar pedidos.")

    doc.add_page_break()

    # --------------------------
    # 6. Metodología
    # --------------------------
    add_title(doc, "6. Metodología", level=1)

    add_title(doc, "6.1. Enfoque de investigación", level=2)
    add_paragraph(doc, "El trabajo se basó en una investigación aplicada con enfoque cualitativo-cuantitativo, ya que buscaba resolver un problema práctico (mejorar la gestión de procesos en PyMEs de muebles) mediante la combinación de: análisis de procesos productivos (cualitativo), modelado de sistemas (estructurado), propuesta de solución técnica.")

    add_title(doc, "6.2. Métodos de recolección de datos", level=2)
    add_list_item(doc, "Investigación documental: Revisión de materiales de la materia Producción y Materiales (Unidades 1 a 8), bibliografía sobre ERP, gestión de inventarios y procesos productivos, guía del trabajo final de la materia.")
    add_list_item(doc, "Análisis de procesos: Elaboración de Diagrama de Operaciones del Proceso (DOP), elaboración de Diagrama de Análisis del Proceso (DAP), identificación de cuellos de botella y oportunidades de mejora.")
    add_list_item(doc, "Herramientas de Inteligencia Artificial: Asistentes conversacionales para apoyo en la estructuración del proyecto, verificación de conceptos técnicos, elaboración de diagramas y modelos iniciales.")
    add_list_item(doc, "Modelado de sistemas: Diagrama Entidad-Relación (ER) para la base de datos, diagramas UML de clases para el diseño del sistema.")

    doc.add_page_break()

    # --------------------------
    # 7. Desarrollo y Análisis
    # --------------------------
    add_title(doc, "7. Desarrollo y Análisis", level=1)

    add_title(doc, "7.1. Definición del nicho de mercado", level=2)
    add_paragraph(doc, "El nicho elegido son las PyMEs de fabricación de muebles de madera (5 a 50 empleados), ya que: tienen dolores claros y urgentes: control de inventario deficiente, seguimiento manual de órdenes; son numerosas y tienen potencial de adopción de tecnologías; necesitan integración con ecommerce para competir en el mercado actual.")
    add_paragraph(doc, "Los dolores principales identificados son:")
    add_list_item(doc, "Control de inventario de materias primas manual (hojas de cálculo o papel)")
    add_list_item(doc, "Seguimiento de órdenes de producción sin visibilidad en tiempo real")
    add_list_item(doc, "Poca información sobre costos reales de fabricación")
    add_list_item(doc, "Sin conexión entre ventas online y procesos internos")

    add_title(doc, "7.2. Análisis del proceso productivo de muebles de madera", level=2)
    add_title(doc, "7.2.1. Diagrama de Operaciones del Proceso (DOP)", level=3)
    add_paragraph(doc, "(Nota: El diagrama gráfico DOP se deberá crear con herramientas como Draw.io, Lucidchart o similar y agregar en esta sección. A continuación, una representación textual:)")
    add_list_item(doc, "Paso 1: Recepcionar MP (Recepción de materias primas: madera, herrajes, pintura) – 15 min")
    add_list_item(doc, "Paso 2: Almacenar MP (Almacenamiento en depósito de materias primas) – 10 min")
    add_list_item(doc, "Paso 3: Cortar madera (Corte y dimensionado de piezas de madera) – 30 min")
    add_list_item(doc, "Paso 4: Mecanizar (Perforación, rebajado, moldeado) – 25 min")
    add_list_item(doc, "Paso 5: Ensamblar (Unión de las piezas para formar la estructura del mueble) – 40 min")
    add_list_item(doc, "Paso 6: Lijar (Preparación de la superficie para el acabado) – 20 min")
    add_list_item(doc, "Paso 7: Acabar (Pintura o barnizado) – 45 min + secado")
    add_list_item(doc, "Paso 8: Controlar calidad (Verificación de especificaciones) – 10 min")
    add_list_item(doc, "Paso 9: Embalar (Empaque para envío o venta) – 15 min")
    add_list_item(doc, "Paso 10: Almacenar PT (Almacenamiento en depósito de productos terminados) – 10 min")

    add_title(doc, "7.2.2. Diagrama de Análisis del Proceso (DAP)", level=3)
    add_paragraph(doc, "(Nota: El diagrama gráfico DAP se deberá crear con herramientas como Draw.io, Lucidchart o similar y agregar en esta sección. A continuación, una representación textual:)")
    add_list_item(doc, "Paso 1: O – Recepcionar MP – 15 min")
    add_list_item(doc, "Paso 2: T – Trasladar a depósito – 20 m")
    add_list_item(doc, "Paso 3: A – Almacenar MP – 10 min")
    add_list_item(doc, "Paso 4: T – Trasladar a taller – 30 m")
    add_list_item(doc, "Paso 5: O – Cortar madera – 30 min")
    add_list_item(doc, "Paso 6: I – Inspección parcial – 5 min (Oportunidad de mejora)")
    add_list_item(doc, "Paso 7: O – Mecanizar – 25 min")
    add_list_item(doc, "Paso 8: O – Ensamblar – 40 min")
    add_list_item(doc, "Paso 9: O – Lijar – 20 min")
    add_list_item(doc, "Paso 10: O – Acabar – 45 min")
    add_list_item(doc, "Paso 11: D – Secado – 120 min")
    add_list_item(doc, "Paso 12: I – Control de calidad final – 10 min")
    add_list_item(doc, "Paso 13: O – Embalar – 15 min")
    add_list_item(doc, "Paso 14: T – Trasladar a depósito PT – 25 m")
    add_list_item(doc, "Paso 15: A – Almacenar PT – 10 min")
    add_paragraph(doc, "Oportunidades de mejora identificadas: Control de inventario digital, seguimiento de órdenes en tiempo real, reducción de tiempos de traslado, integración con ecommerce.")

    add_title(doc, "7.3. Modelado del sistema ERP", level=2)
    add_title(doc, "7.3.1. Modelo Entidad-Relación (ER)", level=3)
    add_paragraph(doc, "(Nota: El diagrama ER gráfico se encuentra en la carpeta docs/03-modelo-er.md y se deberá exportar como imagen y agregar aquí.)")
    add_paragraph(doc, "El modelo ER incluye 15 entidades principales: Category (categorías de productos), Product (productos terminados), RawMaterial (materias primas), Supplier (proveedores), ProductionOrder (órdenes de producción), ProductionStage (etapas de producción), StageLog (registros de etapas), MaterialConsumption (consumo de MP), BillOfMaterials (lista de materiales), Customer (clientes), Order (pedidos de clientes, con flag isEcommerce), OrderItem (items del pedido), User (usuarios del sistema), PurchaseOrder (órdenes de compra), PurchaseItem (items de compra).")

    add_title(doc, "7.3.2. Diagramas UML de clases", level=3)
    add_paragraph(doc, "(Nota: Los diagramas UML completos se encuentran en la carpeta docs/04-uml-clases.md y se deberán exportar como imágenes y agregar aquí.)")
    add_paragraph(doc, "Se diseñaron diagramas UML de clases para todas las entidades del dominio, con atributos, métodos y relaciones. Destacan: ProductionOrder con relación a Product, StageLog y MaterialConsumption; Order con relación a Customer y OrderItem, y atributo isEcommerce para diferenciar pedidos online; User con atributo role para control de acceso (ADMIN, PRODUCCION, VENTAS, ALMACEN).")

    add_title(doc, "7.4. Diseño de la arquitectura técnica", level=2)
    add_title(doc, "7.4.1. Backend con Spring Boot", level=3)
    add_paragraph(doc, "El backend se desarrolló con Spring Boot 3.2 (Java 17), con la siguiente estructura: entity/ (Entidades JPA mapeadas a la BD), repository/ (Repositorios Spring Data JPA), service/ (Servicios de negocio), controller/ (Controladores REST API), security/ (Autenticación y autorización JWT).")
    add_paragraph(doc, "Base de datos: H2 para desarrollo (en memoria), MySQL para producción.")

    add_title(doc, "7.4.2. Frontend con Angular", level=3)
    add_paragraph(doc, "El frontend se desarrolló con Angular 17, con: componentes standalone, rutas para navegación, servicios para consumo de la API REST, interfaz de usuario adaptada a equipos no técnicos.")

    add_title(doc, "7.5. Integración con ecommerce", level=2)
    add_paragraph(doc, "El sistema está preparado para:")
    add_list_item(doc, "Sincronización de inventario: El campo stock de Product se actualiza automáticamente y se envía al ecommerce.")
    add_list_item(doc, "Flujo de pedidos online: Cuando un cliente compra en el ecommerce, se crea un Order en el ERP con isEcommerce = true.")
    add_list_item(doc, "Visibilidad para clientes: Los clientes pueden ver el estado de su pedido en tiempo real.")
    add_list_item(doc, "Actualización de estado: Cuando la orden de producción se completa, el estado del pedido online se actualiza automáticamente.")

    add_paragraph(doc, "")
    add_title(doc, "7.6. Aplicación de IA e Industria 4.0", level=2)
    add_list_item(doc, "Mantenimiento predictivo: Algoritmos de ML para predecir fallos en máquinas de corte y lijado, basados en datos de vibración y temperatura.")
    add_list_item(doc, "Optimización de inventario: IA para predecir demanda de materias primas y calcular puntos de pedido automáticos.")
    add_list_item(doc, "Control de calidad por visión artificial: Cámaras en la estación de pintura para detectar defectos de acabado.")
    add_list_item(doc, "Planificación automática: IA para priorizar órdenes de producción según fechas de entrega y disponibilidad de MP.")

    doc.add_page_break()

    # --------------------------
    # 8. Conclusiones
    # --------------------------
    add_title(doc, "8. Conclusiones", level=1)
    add_paragraph(doc, "El trabajo permitió aplicar los conocimientos adquiridos en la materia Producción y Materiales al diseño de un ERP especializado para PyMEs de fabricación de muebles de madera.")
    add_paragraph(doc, "Hallazgos principales: Relevancia del tema: las PyMEs de muebles tienen dolores claros y urgentes que un ERP puede resolver; Importancia del análisis de procesos: los diagramas DOP y DAP permitieron identificar oportunidades de mejora; Integración de ecommerce es clave: en el mercado actual, las empresas necesitan sincronizar sus procesos internos con las ventas online; IA e Industria 4.0 tienen potencial: aplicaciones como mantenimiento predictivo y control de calidad por visión artificial pueden generar una gran ventaja competitiva.")
    add_paragraph(doc, "Mejoras propuestas: Implementar el ERP en una PyME piloto, capacitar al personal, medir indicadores (KPIs), escalar gradualmente.")
    add_paragraph(doc, "Este trabajo demuestra que las PyMEs no necesitan invertir millones en sistemas de gestión complejos. Un ERP especializado, de bajo costo y fácil de usar, puede mejorar significativamente su eficiencia y competitividad. Además, la integración de la IA, como parte de la Industria 4.0, no es solo una tendencia, sino una necesidad para las empresas que quieren sobrevivir y crecer en el mercado actual.")

    doc.add_page_break()

    # --------------------------
    # 9. Referencias
    # --------------------------
    add_title(doc, "9. Referencias", level=1)
    add_paragraph(doc, "Chase, R. B., Jacobs, F. R., & Aquilano, N. J. (2021). Operations Management for Competitive Advantage (14.ª ed.). McGraw-Hill Education.")
    add_paragraph(doc, "Moscardo, E. (2020). Producción y Materiales: Teoría y Ejercicios Aplicados. [Editorial].")
    add_paragraph(doc, "Monk, E. F., & Wagner, B. J. (2013). Enterprise Resource Planning (4.ª ed.). Cengage Learning.")
    add_paragraph(doc, "Ministerio de Producción de la Nación. (2022). Guía para PyMEs de la Industria Mueblera. Buenos Aires.")
    add_paragraph(doc, "Lasi, H., Fettke, P., Kemper, H. G., Feld, T., & Hoffmann, M. (2014). Industry 4.0. Business & Information Systems Engineering, 6(4), 239-242.")
    add_paragraph(doc, "Joaquín, I. (2026). Material de Clase de la Materia Producción y Materiales. Universidad Nacional de [X].")
    add_paragraph(doc, "Spring Boot Documentation. (2024). Recuperado de https://spring.io/projects/spring-boot")
    add_paragraph(doc, "Angular Documentation. (2024). Recuperado de https://angular.io/docs")

    doc.add_page_break()

    # --------------------------
    # 10. Anexos
    # --------------------------
    add_title(doc, "10. Anexos", level=1)

    add_title(doc, "10.1. Anexo A — Declaración de uso de Inteligencia Artificial", level=2)
    add_paragraph(doc, "Los integrantes del grupo declaramos que hemos usado herramientas de Inteligencia Artificial como apoyo en la realización de este trabajo final, de acuerdo con las disposiciones de la guía de la materia.")
    add_paragraph(doc, "Herramientas de IA utilizadas: Asistentes conversacionales (Trae IDE), copilots de código (para estructuración del proyecto Spring Boot y Angular).")
    add_paragraph(doc, "Ejemplos de prompts utilizados: Crear un modelo Entidad-Relación para un ERP de fabricación de muebles de madera; Estructurar un proyecto Spring Boot con JPA y MySQL; Elaborar un diagrama DOP para el proceso de fabricación de un mueble; Redactar un marco teórico sobre gestión de inventario en PyMEs.")
    add_paragraph(doc, "Resultados validados y adoptados: Estructura del proyecto Spring Boot y Angular, entidades JPA y repositorios, diagramas DOP y DAP iniciales (luego ajustados manualmente), marco teórico (luego revisado y complementado con bibliografía de la materia), guía de entrevistas con clientes potenciales.")
    add_paragraph(doc, "Resultados descartados y por qué: Algunas sugerencias de arquitectura muy complejas, no aptas para PyMEs (descartadas porque el nicho necesita simplicidad); Alguna información incorrecta sobre métodos de gestión de inventario (descartada y reemplazada por contenido de la bibliografía de la materia); Código generado automáticamente sin comentarios (revisado y ajustado manualmente).")
    add_paragraph(doc, "Todo el contenido del trabajo fue revisado, ajustado y validado por los integrantes del grupo. Las afirmaciones, datos y citas bibliográficas son responsabilidad exclusiva de los autores.")
    add_paragraph(doc, "")
    add_paragraph(doc, "Firmas de los integrantes:")
    add_paragraph(doc, "[Integrante 1]")
    add_paragraph(doc, "[Integrante 2]")
    add_paragraph(doc, "[Integrante 3]")
    add_paragraph(doc, "[Integrante 4]")
    add_paragraph(doc, "[Integrante 5]")
    add_paragraph(doc, "")
    add_paragraph(doc, "Fecha: [DD/MM/2026]")

    add_title(doc, "10.2. Anexo B — Material de apoyo", level=2)
    add_paragraph(doc, "(Nota: Agregar aquí las imágenes de los diagramas DOP, DAP, ER, UML, así como el listado de archivos del proyecto.)")

    # Guardar el documento
    output_file = "Monografia-Trabajo-Final.docx"
    doc.save(output_file)

    print(f"✅ ¡Monografía generada exitosamente!")
    print(f"📄 Archivo: {output_file}")


if __name__ == "__main__":
    main()

