#ejercio 2
# defenir las variables de la suma de los numeros
sumaPositivos = 0
# variable repetiva para conventir los numeros negativos en positivo y hacerlo suma 
for i in range(10):
    numeroIngresado = int(input("Ingrese un número negativo: "))
    if numeroIngresado < 0:
        numeroPositivo = abs(numeroIngresado)
        sumaPositivos += numeroPositivo
    else:
        print("El número ingresado no es negativo.")
#impresion leer la suma de los numeros convertidos
print(f"La suma de los números convertidos a positivos es: {sumaPositivos}")
