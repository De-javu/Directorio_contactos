#  cremos el archiv con la logica
import sys, json , csv

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
    

# Esta funcion se encarga de cargar los archivos cada vez que s eocrre el programa, para tener los datos disponibles
def cargar_contactos():
    try:
       with open('contactos.json') as archivo:
         return json.load(archivo)
   
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


# Esta funcion seencarga de almacenar los datos en formato csv    
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

    

def buscar_contacto(lista, nombre):
    #logica para buscar nombre
    pass

def listar_contactos(lista):
    # logica para listar contactos
    pass


# sta funcion se encarga de almacenar los datos ingresados en json y csv en un solo paso 
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
    
 

def cargar_csv(listas):
    # losgica para cargar csv
    pass

def cargar_json(lista):
    # logica para cargar json
    pass


def salir():
    print("Gracias por utilizar nuestro directorio")
    sys.exit()
    