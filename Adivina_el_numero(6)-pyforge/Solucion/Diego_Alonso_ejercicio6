import random
import os

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpiar_terminal()

def adivina_numero():
    #creamos un numero random del 1 al 100
    numero = random.randint(1, 100)

    intentos = 0

    while True:
        #obtenemos el valor dado por el usuario
        intento = int(input("Adivina el número (entre 1 y 100): "))
        #cada intento suma la variable
        intentos += 1
        #si el valor dado por el usuario es menor al numero 
        if intento < numero:
            limpiar_terminal()
            print("El número es mayor.")
        #si el valor dado por el usuario es mayor al numero 
        elif intento > numero:
            limpiar_terminal()
            print("El número es menor.")
         #si el valor dado por el usuario es correcto
        else:
            limpiar_terminal()
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_numero()