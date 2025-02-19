import re

ingreso_clase_baja = 500000
ingreso_clase_media = 2500000
ingreso_clase_alta = 10000000

def validar_numeros():
	"""
	Funcion para validar que el usuario ingrese el dato deseado
	
	Retorna un numero tipo: Float
	"""
	while True:
		try:
			numero = float(input("Ingresa la cantidad: "))
			if numero >= 0.0:
				return numero
			else:
				print("Numero negativo no valido")
		except ValueError:
			print("Dato invalido")
			
def validar_nombre():
	"""
	Valida que el nombre sea valido (Solo letras y espacios, nada de numeros)
	"""
	while True:
		nombre = input("Ingresa tu nombre: ")
		if re.match(r"^[A-Za-z\s]+$" , nombre):
			return nombre
		else:
			print("Ingresa un nombre valido.")
			
def validar_edad():
	"""
	Se valida una edad valida (mayor que 0 y menor que 120)
	"""
	while True:
		try:
			edad = int(input("Ingreda tu edad: "))
			if edad > 0 and edad < 120:
				return edad
			else:
				print("Edad invalida")
		except ValueError:
			print("Dato invalido")	

def pedir_datos():
	#Se solicita el nombre y edad
	return validar_nombre() , validar_edad()
	
def ingresos_totales():
	# Funcion para pedir ingresos por trabajo, inversiones, activos y retorna la suma de todos los ingresos
	
	print(" Ingresos por trabajo")
	trabajo = validar_numeros()
	print("\n Ingresos por inversiones")
	inversiones = validar_numeros()
	print("\n Ingresos por activos")
	activos = validar_numeros()
	return trabajo + inversiones + activos
	
	
def gastos_totales():
	# Funcion para pedir los gastos de impuestos, lujos, deudas y otros gastos que puedan haber, retorna la suma de todos los gastos
	
	print(" Gasto en impuestos")
	impuestos = validar_numeros()
	print("\n Gasto en lujos")
	lujos = validar_numeros()
	print("\n Gasto en deudas")
	deudas = validar_numeros()
	print("\n Otros Gastos")
	otros_gastos = validar_numeros()
	return impuestos + lujos + deudas + otros_gastos
	
def ingreso_neto(ingresos , gastos):
	# Pide los ingresos y gastos totales para retornar el ingreso neto
	
	return ingresos - gastos 
	
def definir_clase_social(ingreso_neto):
	
	"""
	 Solicita el ingreso neto y verifica la clase social 
	 
	 Clase Baja: menor que 500.000 COP 
	 Clase Media: Mayor que 500000 (clase baja) y menor que 10000000 (clase alta) COP
	 Clase Alta: Mayor que 10.000.000 COP
	"""
	
	if ingreso_neto <= ingreso_clase_baja:
		return "Perteneces a la clase Baja"
	elif ingreso_neto > ingreso_clase_baja and ingreso_neto <= ingreso_clase_alta:
		return "Perteneces a la clase Media"
	else:
		return "Perteneces a la clase Alta"
	
def calcular_porcentaje(ingreso_neto):
	# Retorna el porcentaje del ingreso neto respecto al ingreso de la clase alta
	
	return ingreso_neto / ingreso_clase_alta * 100
	

		
def main():
	# Funcion principal :v
	
	nombre , edad = pedir_datos() # Nombre y edad

	ingresos = ingresos_totales() # Ingresos
	
	gastos = gastos_totales() # Gastos
	
	neto = ingreso_neto(ingresos , gastos) # Ingreso neto
	
	clase = definir_clase_social(neto) # Clase social
	porcentaje = calcular_porcentaje(neto)
	
	print(f"{clase} , el porcentaje de tus ingresos comparados a los de la clase alta es de {porcentaje}%")
	
	
	
if __name__ == "__main__":
	main()
	
