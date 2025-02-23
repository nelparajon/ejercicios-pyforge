import os

contacts = {}
status = True

def list_contacts():
    for valor in contacts:
        print(valor , "num", contacts[valor])

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpiar_terminal()

while status == True:
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Salir")

    opcion = input("Ingrese accion : ")

    if opcion == "1":
        limpiar_terminal()
        nombre = input("Ingrese el nombre: ")
        numero = input("Ingrese numero :")
        if numero[0] == "9" and len(numero) == 9:
           contacts[nombre] = int(numero)   
           limpiar_terminal()    
           print("Contacto agregado")
        else:
            limpiar_terminal()
            print("Numero invalido")

    elif opcion == "2":
        limpiar_terminal()
        list_contacts()

    elif opcion == "3":
        limpiar_terminal()
        list_contacts()
        nombre = input("Ingrese el nombre del contacto a eliminar : ")
        del(contacts[nombre])
        limpiar_terminal()
        print("Contacto eliminado")

    elif opcion == "4":
        limpiar_terminal()
        print("Saliendo...")
        limpiar_terminal()
        status = False
    
    else:
        limpiar_terminal()

        print("Opcion invalida")
        
    

