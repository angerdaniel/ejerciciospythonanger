# Ejercicio 7
cantidadAutos = int(input("Ingrese la cantidad total de autos: "))
contadorRojo = 0
contadorVerde = 0
contadorAmarillo = 0
contadorAzul = 0
contadorBlanco = 0

for i in range(cantidadAutos):
    placaAuto = input("Ingrese el último dígito de la placa del auto: ")
    ultimoDigitoPlaca = int(placaAuto[-1])
    
    if ultimoDigitoPlaca == 1 or ultimoDigitoPlaca == 2:
        contadorRojo += 1
    elif ultimoDigitoPlaca == 3 or ultimoDigitoPlaca == 4:
        contadorVerde += 1
    elif ultimoDigitoPlaca == 5 or ultimoDigitoPlaca == 6:
        contadorAmarillo += 1
    elif ultimoDigitoPlaca == 7 or ultimoDigitoPlaca == 8:
        contadorAzul += 1
    elif ultimoDigitoPlaca == 9 or ultimoDigitoPlaca == 0:
        contadorBlanco += 1

print(f"Rojo: {contadorRojo}, Verde: {contadorVerde}, Amarillo: {contadorAmarillo}, Azul: {contadorAzul}, Blanco: {contadorBlanco}")