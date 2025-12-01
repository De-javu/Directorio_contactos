# Pagina principla para ejecucion  del programa:

from contactos import agregar_contacto, buscar_contacto, listar_contactos, salir, guardar_contactos_json 
# Se crea la funcion de menu de opciones
def mostrar_menu():
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Listar todos los contactos")
    print("4. Gurdar contactos en el CSV")
    print("5. Guardar contactos en el archivo JSON ")
    print("6. Cargar contactos desde archivo CSV")
    print("7. Cargar contactos desde archivo JSON")
    print("8. Salir")


# Se crea la funcion programa , que la que da la entrada para interactuar con las funciones del menu
def programa():
    contactos = []
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opcion  "))
        if opcion == 1:
            agregar_contacto(contactos)
        elif opcion == 4:
            
            pass
        elif opcion == 5:
            guardar_contactos_json(contactos) 
        
        elif opcion == 8:
            salir()     

           
        


# permite definir cuando se corra el programa en que funciondebe iniciar para que se ejecute de forma ordenada
if __name__ == "__main__":
    programa()

    