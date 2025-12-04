#  creamos el archivo con la logica
import  json , csv, sys

#  Esta funcion se encarga de agregar contactos y listarlos en una lista
def agregar_contacto(lista):
    while True:
        nombre = input("Digta el Nombre: ")
        if nombre  == "":
            print("///////////////////////////////////////")
            break
        telefono = input("Digita el numero telefonico: ")
        email = input("Digita el correo electronico ") 
        lista.append({'nombre': nombre, 'telefono': telefono, 'email': email}) # Agrega un nuevo contacto a la lista
    guardar_contactos(lista)
    

# Se crea una funcion que carga los archivos que almacenan los contactos y le damos manejo por, por medio de try
def cargar_contactos():
    try:
       with open('contactos.json') as archivo:
         contenido =archivo.read()
         if not contenido.strip():
             return []
         return json.loads(contenido)
   
    except FileNotFoundError:
        print("El archivo no existe")
        return[  ]


# Esta funcion se encarga de almacenar los datos ingresados en formato json
def guardar_contactos_json(lista):
    while True:
        nombre = input("Digta el Nombre: ")

        if nombre  == "":
            print("///////////////////////////////////////")
            break
        telefono = input("Digita el numero telefonico: ")
        email = input("Digita el correo electronico ") 
        lista.append({'nombre': nombre, 'telefono': telefono, 'email': email}) # Agrega un nuevo contacto a la lista

        # Se gurda la lista en un  archivo json 
        nombre_json = 'contactos.json' 
        with open(nombre_json, 'w') as archivo:
            json.dump(lista, archivo, indent=4)
        print("Contactos guardados en el archivo.json")


# Esta funcion se encarga de almacenar los datos en formato csv    
def guardar_contactos_csv(lista):
    while True:
        nombre = input("Digta el Nombre: ")
        if nombre  == "":
            print("///////////////////////////////////////")
            print("")
            break
        telefono = input("Digita el numero telefonico: ")
        email = input("Digita el correo electronico ") 
        lista.append({'nombre': nombre, 'telefono': telefono, 'email': email}) # Agrega un nuevo contacto a la lista
        # Se almacena la lista en un archivo csv
        nombre_csv = 'contactos.csv' 
        with open(nombre_csv, mode='w', newline='') as archivo:
            campos = ['nombre', 'telefono', 'email']
            writer = csv.DictWriter(archivo, fieldnames=campos) # Crea el objeto writer
            writer.writeheader()           # Escribe los encabezados
            writer.writerows(lista)  # Escribe todas las filas de la lista
        print("Contactos guardados en el archivo.csv")

    
# Se crea el sistema para buscar contactos 
def buscar_contacto(lista, nombre=None):
    if not nombre:
        nombre = input("Escribe el nombre de la persona que buscas: ")
    with open('contactos.json', 'r') as archivo:
        data = json.load(archivo)
        for contacto in data:
            if contacto['nombre'].lower() == nombre.lower():
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print("Contacto enconytrado en el archivo json")
                break
        else:
            print("Contacto no encontrado.")

    with open('contactos.csv', mode='r', newline='') as archivo_csv:
        lector =csv.DictReader(archivo_csv)
        for contacto in lector:
            if contacto['nombre'].lower() == nombre.lower():
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print("contacto encontrado en el archiov csv")
                break
        else:
            print("Contacto no encontrado.")




# Aca se crea una funcion para listar contactos
def listar_contactos(lista):
    with open('contactos.json', 'r') as archivo:
        lista =json.load(archivo)
        print("\n======= LISTA DE CONTACTOS          JSON       =======")
    for contactos in lista:
        print(f'NOMBRE: {contactos['nombre']},TELEFONO: {contactos['telefono']}, CORREO: {contactos['email']},')
        print('***********************Listado de tu archivo json ********************************')

    with open('contactos.csv', mode='r', newline='') as archivo_csv:
        lista = csv.DictReader(archivo_csv)
        print("\n======= LISTA DE CONTACTOS          CSV       =======")
        for contacto in lista:
            print(f"NOMBRE: {contacto['nombre']}, TELEFONO: {contacto['telefono']}, CORREO: {contacto['email']}")
    print('***********************Listado de tu archivo csv ********************************')
    


# Esta funcion se encarga de almacenar los datos ingresados en json y CSV en un solo paso 
def guardar_contactos(lista):
    # Se gurda la lista en un  archivo json 
    nombre_json = 'contactos.json' 
    with open(nombre_json, 'w') as archivo:
         json.dump(lista, archivo, indent=4)
 
    # Se almacena la lista en un archivo csv
    nombre_csv = 'contactos.csv' 
    with open(nombre_csv, mode='w', newline='') as archivo:
        campos = ['nombre', 'telefono', 'email']
        writer = csv.DictWriter(archivo, fieldnames=campos) # Crea el objeto writer
        writer.writeheader()           # Escribe los encabezados
        writer.writerows(lista)  # Escribe todas las filas de la lista
    print("Contactos guardados en contactos.json y contactos.csv")
    
 
# Esta funiocn permite cargar el archivo CSV
def cargar_csv(lista):
    with open('contactos.csv', mode='r', newline='') as archivo_csv:
        lista = csv.DictReader(archivo_csv)
        print("\n======= LISTA DE CONTACTOS =======")
        for contacto in lista:
            print(f"NOMBRE: {contacto['nombre']}, TELEFONO: {contacto['telefono']}, CORREO: {contacto['email']}")
    print('Listado de tu archivo csv')

# Esta funcion permite cargar el archivo json
def cargar_json(lista):
    with open('contactos.json', 'r') as archivo:
        lista =json.load(archivo)
    for contactos in lista:
        print(f'NOMBRE: {contactos['nombre']},TELEFONO: {contactos['telefono']}, CORREO: {contactos['email']},')

# Esta funcion permite salir del bucle del menu del programa 
def salir():
    print("Gracias por utilizar nuestro directorio")
    sys.exit()
    