# Pagina principla para ejecucion  del programa:

import contactos

# Se crea la funcion de menu de opciones
def mostrar_menu():
    print(" ************Menu de Opciones************")
    print(" ")
    print("1. Agregar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Listar todos los contactos")
    print("4. Gurdar contactos en el CSV")
    print("5. Guardar contactos en el archivo JSON ")
    print("6. Cargar contactos desde archivo CSV")
    print("7. Cargar contactos desde archivo JSON")
    print("8. Salir")
    print(" ****************************************")


# Se crea la funcion programa , que la que da la entrada para interactuar con las funciones del menu
def programa():
    lista = contactos.cargar_contactos()
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opcion  "))
        if opcion == 1:
            contactos.agregar_contacto(lista)
        elif opcion == 2:
            contactos.buscar_contacto(lista)
        elif opcion == 3: 
            contactos.listar_contactos(lista)
        elif opcion == 4:
             contactos.guardar_contactos_csv(lista)
        elif opcion == 5:
            contactos.guardar_contactos_json(lista) 
        elif opcion == 6:
            contactos.cargar_csv(lista)
        elif opcion ==7:
            contactos.cargar_json(lista)    
        elif opcion == 8:
            contactos.salir()     

           

# permite definir cuando se corra el programa en que funciondebe iniciar para que se ejecute de forma ordenada
if __name__ == "__main__":
    programa()

    