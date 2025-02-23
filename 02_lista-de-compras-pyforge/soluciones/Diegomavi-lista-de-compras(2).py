import os


products = {}
status = True

def list_product():
    for valor in products:
        print(valor,"-", products[valor])

def limpiar_terminal():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

limpiar_terminal()


while status == True:

    eleccion = input("Nombre del producto o (help) para obtener comandos : ").lower()

    if eleccion == "salir":
        limpiar_terminal()
        list_product()
        status = False
    elif eleccion == "lista":
        limpiar_terminal()
        list_product()
    elif eleccion == "eliminar":
        limpiar_terminal()
        list_product()
        erase = input("Que producto desea eliminar : ")
        del(products[erase])
        limpiar_terminal()
        print("Producto Eliminado")
    elif eleccion == "help":
        limpiar_terminal()
        print("comandos : lista - eliminar - salir")
    else:
        products[eleccion] = int(input("cantidad : "))
        limpiar_terminal()

