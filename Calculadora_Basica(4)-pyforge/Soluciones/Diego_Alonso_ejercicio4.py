

def caculadora():
    #Pedimos la operacion
    calculo = input("Tipo de operacion suma/resta/division/multiplicacion : ")
    #si la operacion ingresada existe se da como valido
    if calculo == "suma" or calculo == "resta" or calculo == "division" or calculo == "multiplicacion":
      print("Operacion elegida : ", calculo)
    # si la operacion ingresada no existe se vuelve a pedir otra operacion
    else:
      print("Operacion invalida")
      caculadora()
    #pedimos los numeros a operar
    num1 = input("Primer numero : ")
    num2 = input("Segundo numero : ")
    #para no repetir el mismo texto se crea una variable
    result = "El resultado es :"

    #se realiza la operacion elegida anteriormente
    if calculo == "suma":
      print(result , int(num1) + int(num2))
  
    elif calculo == "resta":
      print(result , int(num1) - int(num2))

    elif calculo == "division":
      print(result , int(num1) / int(num2))
    
    elif calculo == "multiplicacion":
      print(result , int(num1) * int(num2))


caculadora()


