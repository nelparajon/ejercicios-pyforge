datos_personales , edad = input("Ingrese nombre") , input("Ingrese Edad")
ing_p_t , ing_p_i , ing_p_a = input("Ingresos por trabajo") , input("Ingreso por inversion ") , input("Ingresos por acciones :")
g_i, g_l , g_d , g_o = input("Ingrese gastos de impuestos :"),input("Ingrese gastos de lujos"),input("Ingrese gastos de deudas :"),input("Ingrese otros gastos")

ing_total = int(ing_p_t) + int(ing_p_i) + int(ing_p_a)
gastos_totales = int(g_i) + int(g_l) + int(g_d) + int(g_o)

ing_neto = int(ing_total) - int(gastos_totales)

clase_baja = 1500
clase_media = 1500
clase_alta = 6000

if ing_neto >= clase_alta: 
     print("Perteneces a la clase alta"),
if ing_neto >= clase_media: #and ing_neto < clase_alta :
     print("perteneces a la clase media"), 
else: 
     print("Perteneces a la clase baja")