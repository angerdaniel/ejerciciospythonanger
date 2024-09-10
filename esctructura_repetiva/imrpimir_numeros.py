#ejercio 1
# defenir las variables de los numeros
contadorPositivos = 0
contadorNegativos = 0
contadorNeutros = 0
# variable repetiva para leer numeros reales
for i in range(20):
    numeroIngresado = int(input("Ingrese un número : "))
    if numeroIngresado > 0:
        contadorPositivos += 1
    elif numeroIngresado < 0:
        contadorNegativos += 1
    else:
        contadorNeutros += 1

#impresion leer número real y saber  cuanto nuemros uno
print(f"Positivos: {contadorPositivos}, Negativos: {contadorNegativos}, Neutros: {contadorNeutros}")

