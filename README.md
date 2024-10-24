# OnlyPets

# Proyecto OnlyPets

Este proyecto es una aplicación web de ventas enfocada en productos para mascotas, específicamente perros. Utiliza Django como framework backend y Bootstrap para el diseño frontend. A continuación, se detalla el proceso de desarrollo realizado hasta ahora.

## Requisitos

- Python 3.x
- Django 4.x
- Bootstrap 5.x

## Estructura del Proyecto

- **base.html**: Plantilla base que contiene la estructura común de la aplicación.
- **index.html**: Página principal que muestra un carrusel de imágenes de perritos y tarjetas de productos.
- **static/**: Carpeta que contiene archivos estáticos como imágenes y CSS.
  - **img/**: Imágenes de productos y del carrusel.
  - **css/**: Archivos CSS para estilos personalizados.

## Pasos Realizados

1. **Configuración del Entorno**:

   - Creación de un entorno virtual en la carpeta del proyecto.
   - Instalación de Django utilizando `pip`.

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   pip install django
   ```

## Creacion paso

- Inicialización del proyecto Django y creación de una aplicación llamada onlypets.

```bash
   django-admin startproject onlypets
cd onlypets
python manage.py startapp ventas

```

## Estructura de Plantillas:

Se creó la plantilla base base.html para compartir estructura en las páginas.
Se desarrolló la página index.html con un carrusel de imágenes y tarjetas de productos.
Implementación del Carrusel:
Se utilizó Bootstrap para implementar un carrusel que muestra imágenes de perritos. El carrusel incluye botones para navegar entre las imágenes.

## Desarrollo de Tarjetas de Productos:

Se añadieron tarjetas de productos con descripciones y botones de compra en la misma página.
Integración de Archivos Estáticos:
Se configuró Django para servir archivos estáticos y se organizaron imágenes y estilos en sus respectivas carpetas.
Ejecución del Proyecto

Para ejecutar el proyecto en un entorno local:

Asegúrate de que el entorno virtual esté activado.
Navega hasta la carpeta del proyecto.
Ejecuta el servidor de desarrollo de Django:

```bash
python manage.py runserver
Accede a la aplicación en tu navegador en http://127.0.0.1:8000/.

```

Contribuciones
Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios.
