# Lista de las boletas
descuentosBoletas = [
    {"color": "rojo", "descuento": 0.15},
    {"color": "verde", "descuento": 0.20}
]

# Datos de la compra hechas por el usuario para la lista
totalCompra = float(input('Total de la compra: '))

# Datos del color de la boleta para el descuento del usuario
colorDeLaBoleta = input("Ingrese el color de la boleta (rojo, verde, otro color): ").strip().lower()

# Definir los valores de los colores para el descuento
if colorDeLaBoleta == 'rojo': 
    porcentajeDelDescuento = 0.15
elif colorDeLaBoleta == 'verde':
    porcentajeDelDescuento = 0.20
else:
    porcentajeDelDescuento = 0.00

# La variable para calcular el descuento
descuento = totalCompra * porcentajeDelDescuento

# La variable del total de la compra con el descuento
totalConDescuento = totalCompra - descuento

# Imprimir los resultados
print(f"Total de la compra: ${totalCompra:.2f}")
print(f"El color de la boleta: {colorDeLaBoleta.capitalize()}")
print(f"El valor del descuento: ${descuento:.2f}")
print(f"El total con descuento es: ${totalConDescuento:.2f}")
