# Proyecto Práctico: Gestor de Contactos (Nivel Básico)

## Objetivo
Crear una aplicación de consola en Python que permita registrar, buscar, listar y guardar contactos usando listas, diccionarios, archivos CSV y JSON.

---

## Requisitos y pasos sugeridos

### 1. Estructura de datos
- Cada contacto será un diccionario con las claves: 'nombre', 'telefono', 'email'.
- Todos los contactos se guardarán en una lista.

### 2. Menú de opciones
- Muestra un menú con las opciones:
    1. Agregar contacto
    2. Buscar contacto por nombre
    3. Listar todos los contactos
    4. Guardar contactos en archivo CSV
    5. Guardar contactos en archivo JSON
    6. Cargar contactos desde archivo CSV
    7. Cargar contactos desde archivo JSON
    8. Salir

### 3. Agregar contacto
- Pide al usuario nombre, teléfono y email.
- Valida que el nombre no exista ya en la lista.
- Valida que el email contenga '@'.
- Agrega el contacto a la lista.

### 4. Buscar contacto
- Pide el nombre a buscar.
- Muestra los datos si existe, o un mensaje si no se encuentra.

### 5. Listar todos los contactos
- Muestra todos los contactos en pantalla, uno por línea.

### 6. Guardar y cargar contactos
- Guarda la lista de contactos en un archivo CSV y en un archivo JSON.
- Permite cargar los contactos desde esos archivos.

### 7. Validaciones
- No permitir nombres duplicados.
- Validar formato de email.

### 8. Documentación y pruebas
- Comenta tu código.
- Prueba todas las funciones antes de darlo por terminado.

---

## Sugerencias
- Usa funciones para cada acción del menú.
- Usa la librería `csv` para archivos CSV y `json` para archivos JSON.
- Puedes guardar los archivos como `contactos.csv` y `contactos.json`.

---

## Entregable
- El código fuente en Python.
- Los archivos de contactos generados.
- (Opcional) Un archivo README.md con instrucciones de uso.

---

Cuando termines cada paso, avísame y revisamos juntos tu avance. ¡Mucho éxito!