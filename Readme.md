# Gestor de Contactos

## Descripción
[Breve descripción de tu proyecto. Este programa se encarga de gestionar un directorio de contactos, permitiendo agregar, buscar, listar y guardar contactos en archivos JSON y CSV.]

## Estructura de archivos
- `main.py`: [Descripción, Archivo principal con el menú y la lógica de interacción.]
- `contactos.py`: [Descripción, Funciones para manipular los contactos y manejar la persistencia.]
- `contactos.json`: [Archivo de almacenamiento en formato JSON.]
- `contactos.csv`: [Archivo de almacenamiento en formato CSV.]
- `VENV`: [Se crea un entorno virtual para persistencias de versiones hasta para otros sistemas operativos      .]

## Requisitos
- Python 3.x

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta del proyecto.

## Ejecución
```bash
python main.py
```

## Uso
- [Explica brevemente cómo usar el programa: agregar, buscar, listar contactos, etc.]

## Ejemplo de función documentada
```python
def menu():
    # Muestra el menú principal y maneja la selección del usuario.
def programa():
    # Es la funcion principal que ejecuta el programa, recibe la opcion de llamado del menu, para ejecutar las funciones correspondientes segun la eleccion del usuario.
def agregar_contacto(lista):
      # Esta funcion se encarga de realizar la logica para almanenar los contactos en los dos formatos a la vez (JSON y CSV).
def buscar_contacto(lista):
    # Esta funcion se encarga de recibir un parametro de busqueda por parte del usuario y se encraga de buscar en las dos lista y devolver el resultado.
def listar_contactos(lista):
    # Esta funcion se encarga de listar los contactos alamcenados en las dos listas (JSON y CSV).
def guardar_contactos_json(lista, filename):
    # Esta funcion se encarga de guaradr directamnete los datos ingresados por teclado en la lista JSON.
def guardar_contactos_csv(lista, filename):
    # Esta funcion se encarga de alamcenar los datos imgresados por teclado en la lista CSV.
def cargar_contactos_json(filename):
    # Esta funcion se encarga de cargar los contactos desde el archivo JSON al iniciar el programa.
def cargar_contactos_csv(filename):
    # Esta funcion se encarga de cargar los contactos desde el archivo CSV al iniciar el programa.
def salir_programa():
    # Esta funcion se encarga de finalizar el programa de manera segura. 
```
## CONCLUSION #
- El proyecto fue clave en el aprendizaje en las diferentes herramientas basicas de python, para el manejo de archivos, tambien se crearon grandes cantidades de funciones las cuales permitieron desarrollar una logica de programacion mas avanzada lo que permite tener el programa  separado si necesito  ajustar mejorar las funciones,  como por ejemplo la validacion del dato que entra sea lo esprado , solo debo ir a esa funcion y no necesito intervenir de nuevo todo el codigo ,  se aprendio muy bien a  resolver la probelmatica para crear los archivos csv y los json 

## Autor
- Nombre: [Andres Pardo]
- Fecha: [2025]

## Licencia
[MIT, GPL, o la que prefieras]
