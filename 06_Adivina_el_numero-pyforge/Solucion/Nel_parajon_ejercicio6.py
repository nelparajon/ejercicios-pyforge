import random

def random_number() -> int:
    return random.randint(1, 100)

def choice_user() -> int:
    return int(input("Introduce un número ente 1 - 100: "))

def compare_numbers(random_number: int, user_num: int):
    #Esta función compara y devuelve el mensaje directamente.
    if user_num == random_number:
        return "es igual"
    elif user_num < random_number:
        return "es menor"
    else:
        return "es mayor"

def menu():
    random_num = random_number()  # Número aleatorio generado al inicio
    print("Bienvenido al juego de adivinar el número.")
    
    while True:
        user_number = choice_user()  #Pedir el número al usuario
        
        result = compare_numbers(random_num, user_number)  # Comparar los números

        if result == "es igual": 
            print(f"Felicidades, adivinaste el número. \n El número era {random_num}")
            break
        else:
            print(f"Tu número {result}. Intenta de nuevo.")  # Si no, muestra el mensaje

#Llamada para iniciar el juego
menu()


        


    