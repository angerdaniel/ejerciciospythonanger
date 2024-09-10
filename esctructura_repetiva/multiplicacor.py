# Ejercicio 4
# Leer el número del que se desea calcular la tabla de multiplicar
numeroMultiplicar = int(input("Ingrese un número para calcular su tabla de multiplicar: "))
# Bucle for para generar la tabla de multiplicar del 1 al 10
for i in range(1, 11):
    productoMultiplicacion = numeroMultiplicar * i
    print(f"{numeroMultiplicar} * {i} = {productoMultiplicacion}")
