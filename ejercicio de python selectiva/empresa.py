# Las variables para obtener los datos del usuario
montoDeLaCompra = float(input("La Compra: "))

# Definir las variables para los porcentajes de inversión
porcentajeInversionPropia = 0.55
porcentajePrestamoBancario = 0.30
porcentajeCreditoFabricante = 0.15

# Definir las variables para obtener los datos asignados por las variables
if montoDeLaCompra > 500000:
    inversionPropia = montoDeLaCompra * porcentajeInversionPropia
    prestamoBancario = montoDeLaCompra * porcentajePrestamoBancario
    creditoFabricante = montoDeLaCompra * porcentajeCreditoFabricante
else:
    inversionPropia = montoDeLaCompra
    prestamoBancario = 0
    creditoFabricante = 0

# Imprimir los resultados
print(f"Monto total de la compra: ${montoDeLaCompra:.2f}")
print(f"Inversión propia: ${inversionPropia:.2f} ({porcentajeInversionPropia * 100:.0f}%)")
print(f"Préstamo bancario: ${prestamoBancario:.2f} ({porcentajePrestamoBancario * 100:.0f}%)")
print(f"Crédito al fabricante: ${creditoFabricante:.2f} ({porcentajeCreditoFabricante * 100:.0f}%)")
