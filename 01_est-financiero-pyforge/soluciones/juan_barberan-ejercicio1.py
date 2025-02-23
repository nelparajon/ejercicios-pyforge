#Crea un programa que evalue el estado financiero del usuario y que diga a que clase economica pertenece:
#Baja, Media, Alta.

#El programa debe pedirle al usuario los siguientes datos:

#Datos personales: nombre, edad.
#Diferentes ingresos: ingreso por trabajo, ingreso por inversiones e ingreso por activos.
#Diferentes gastos: gasto de impuestos, lujos, deudas, y demás

#Calcula el ingreso total, este se obtiene sumando todos los ingresos

#Calcula el gasto total, se hace de la misma manera, suma todos los gatos

#Calcula el ingreso neto = ingresos_totales - gastos_totales

#Busca en internet que ingreso neto debe tener una persona para pertenecer a una de las clases economicas:
#Clase baja, Clase media y Clase alta
#IMPORTANTE: debes buscar esto dependiendo de tu pais
#Una vez que tengas los datos crea 3 variables: ingreso_clase_baja = 25000, y asi sucesivamente

#Crea 3 condicionales (if) que evaluen lo siguiente:
#Si el ingreso neto es mayor o igual al de la clase alta, que muestre en terminal: "Perteneces a la clase alta"
#Si el ingreson neto es mayor o igual al de la clase media, que muestre en terminal: "Perteneces a la clase media"
#Si no se cumple ninguno de los dos que muestre: "Perteneces a la clase baja"

#Opcional:
#Puedes calcular que porcentaje del ingreso de la clase alta y media es el ingreso neto del usuario
#Ayudita: para sacar que porcentaje del ingreso de la clase alta es el ingreso del usuario deben usar esta formula:
#ingreso_neto_usuario / ingreso_clase_alta * 100

#Inicio del programa:

#Importamos colorama para darle color al programa en la terminal:
from colorama import init, Fore, Back, Style
init(autoreset=True)

#Creando funcion que verifique si el valor dado por el usuario es numerico:
def validation_num(i_or_f = 0, *val):
    
    """
    Valida si los valores ingresados son numéricos (enteros o flotantes).

    Parámetros:
    i_or_f (int): 0 para validar enteros, 1 para validar flotantes.
    *val: Valores a validar.

    Retorna:
    list: Lista de valores validados.
    
    """
    
    #Creamos una lista para almacenar los valores finales
    val_final = []

    #Iteramos la lista de numeros ingresados
    for ind, input_value in enumerate(val):
         
        #Declaramos una variable como true para manejar el flujo del bucle
        value = False
        
        #Abrimos el bucle
        while not value:  
        
            try:
                
                #Si recibe como parametro 0 entonces convertimos el valor a int
                if i_or_f == 0:  num = int(input_value)  
                   
                #Si recibimos como parametro 1 entonces convertimos el valor a int   
                elif i_or_f == 1: num = float(input_value)  
                    
                #Si todo sale bien agregamos el numero convertido a va_final y rompemos el bucle
                val_final.append(num)
                value = True 

            #Si ocurre un error:
            except ValueError:
                
                #Mostramos un mensaje:
                print(Fore.LIGHTRED_EX + "ERROR, valor ingresado no válido. Intente de nuevo.")
                
                #Pedimos al usuario que reingrese el valor
                input_value = input(Fore.LIGHTBLACK_EX + f"Reingrese el valor {ind + 1}: ")  

    #Retornamos la lista:
    return val_final

def validation_string(text):
    
    """
    Funcion que valida si el parametro recibido (text) contiene
    numeros, caracteres especiales o espacios, si es asi, se abre un bucle
    hasta que sea solo alfabetico

    """
    
    while not text.isalpha():
            
        print(Fore.RED + "Debes ingresar un valor que NO contenga: Números/Carácteres especiales/Espacios")
        text = input(Fore.LIGHTBLACK_EX + "Vuelve a ingresarlo: ") 
        
    return text     

        
#Pidiendo datos personales al usuario:
nombre, edad = validation_string(input(Fore.LIGHTCYAN_EX + "Ingresa tu nombre: ")), validation_num(0, input( Fore.LIGHTCYAN_EX + "Ingresa tu edad: "))

#Pidiendo diferentes ingresos:
ing_t, ing_i, ing_a = validation_num(1, input(Fore.LIGHTGREEN_EX + "Ingreso ganado por trabajo: "), input("Ingreso ganado por inversiones: ") , input("Ingreso ganado por activos: "))

#Pidiendo diferentes gastos:
g_i, g_l, g_d, g_e = validation_num(0, input(Fore.RED + "Ingresa tus gastos por impuestos:- "), input("Ingresa tus gastos por lujos:- "), input("Ingresa tus gastos por deudas:- ") , input("Ingresa algun gasto extra:- "))

#Definiendo el ingreso y gasto total:
i_total, g_total,  = ing_t + ing_i + ing_a, g_i + g_l + g_d + g_e

#Definiendo el ingreso neto:
i_neto = i_total - g_total

#Definiendo las clases economicas
c_media, c_alta = 1450000, 2160000

#Mostrando datos finales:
print(Fore.LIGHTYELLOW_EX + f"Tu nombre es {nombre.capitalize()}\nTienes {edad} años")
print(Fore.BLUE + f"Ganas ${i_total} al mes\nTus gastos son de -${g_total}\nTu ingreso neto es ${i_neto}")

#Definiendo a que clase economica pertenece el usuario:

#Si el ingreso neto es mayor o igual al de la clase alta, entonces pertenece a esta
if i_neto >= c_alta: print(Fore.YELLOW + "Perteneces a la clase: alta")

#Si el ingreso neto es mayor o igual al de la clase media, entonces pertenece a esta
elif i_neto >= c_media: print(Fore.CYAN + "Perteneces a la clase: media")   
    
#Si no pertenece a ninguna de estas entonces es de clase baja    
else: print(Fore.BLACK + "Perteneces a la clase: baja")  

#Definiendo que porcentaje del ingreso de la clase alta y media es el ingreso neto del usuario:
print(Fore.LIGHTCYAN_EX + f"Tu ingreso neto es el %{((i_neto / c_alta) * 100):.1f} del sueldo de la clase alta\nTu ingreso neto es el %{((i_neto / c_media) * 100):.1f} del sueldo de la clase media")


