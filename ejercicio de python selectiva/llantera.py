cantidadLlantas = int(input("Ingrese la cantidad de llantas que desea comprar: "))

if cantidadLlantas < 5:
    precioPorLlanta = 300000
elif 5 <= cantidadLlantas <= 10:
    precioPorLlanta = 250000
else:
    precioPorLlanta = 200000

totalAPagar = cantidadLlantas * precioPorLlanta
print(f"El total a pagar por {cantidadLlantas} llantas es: ${totalAPagar}")
