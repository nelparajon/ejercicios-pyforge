#Asumo que los usuarios no persisten por tanto solo se quedan guardados mientras el programa corre
users = {}

def add_users():
    """Función para añadir un usuario"""
    print("\n**** ADDING NEW USER ****")
    username = input("Enter username: ")
    phone_number = input("Enter phone number: ")
    users[username] = {'phone': phone_number} #Guardamos el número de teléfono como dict dentro de la key del user
    print(f"User {username} added successfully!")

def update_user():
    """Función para actualizar un usuario"""
    print("\n**** UPDATE USER ****")
    user = input("What user do you want to update? ")
    if user in users: #comprobamos que el usuario exista en el diccionario
        print(f"Current phone: {users[user]['phone']}")
        users[user]['phone'] = input(f"Enter new phone number for {user}: ")
        print(f"User {user} updated successfully!")
    else: #si no existe lo imprimimos
        print(f"User {user} not found.")

def delete_user():
    """Función para borrar un usuario"""
    print("\n**** DELETE USER ****")
    name = input("What user do you want to delete? ")
    if users.pop(name, None): #el método .pop elimina y retorna el usuario, en este caso es None porque solo lo mostramos
        print(f"User {name} was deleted successfully.")
    else:
        print(f"User {name} not found.")

def get_user_by_name():
    """Función para buscar un usuario por su nombre"""
    print("\n**** SEARCH USER ****")
    name = input("Enter username: ")
    print(f"User {name}: {users.get(name, 'Not found')}")

def show_all_users():
    """Función para mostrar todos los usuarios"""
    print("\n**** ALL USERS ****")
    if users:
        for name, data in users.items(): #mostramos nombre y datos de cada usuario
            print(f"User {name}: {data}")
    else:
        print("No users available.")

def exit_program():
    """Función para salir del programa"""
    print("Exiting program. Goodbye!")
    exit()

def menu():
    #diccionario de las funciones para no colapsar con if-elifs con claves-valor
    options = {
        "1": add_users,
        "2": update_user,
        "3": delete_user,
        "4": get_user_by_name,
        "5": show_all_users,
        "6": exit_program
    }

    while True:
        print("\n===== USER MANAGEMENT MENU =====")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Search User by Name")
        print("5. Show All Users")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        action = options.get(choice)

        if action:
            action()  #Llama a la función correspondiente que se haya elegido
        else:
            print("Invalid choice, please try again.")

menu()
