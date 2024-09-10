# Las variables para obtener los datos del usuario
cantidadDeZapatillas = int(input("Ingrese la cantidad de zapatillas: "))
valorDeCompras = float(input("Ingrese el valor de las compras: "))
valorDelDescuento = float(input("Ingrese el valor del descuento de compras (%): "))

# Calculando el descuento   
descuento = (valorDelDescuento * cantidadDeZapatillas) / 100

# Calculando el valor final
valorFinal = valorDeCompras - descuento

# Mostrando el resultado
print("El valor final de la compra es:", valorFinal)
print("La cantidad de zapatillas es:", cantidadDeZapatillas)
print("El valor de compras es:", valorDeCompras)
print("El valor de descuento es:", valorDelDescuento)
