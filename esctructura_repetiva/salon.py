# Ejercicio 6
#la variable para leer la cantidad de personas del salon
cantidadPersonas = int(input("Ingrese la cantidad total de personas en el salón: "))
contadorHombres = 0
contadorMujeres = 0
#Bucle for que recorre el número total de personas en el salón
for i in range(cantidadPersonas):
    sexoPersona = input("Ingrese el sexo de la persona (H/M): ").upper()
    if sexoPersona == 'H':
        contadorHombres += 1
    elif sexoPersona == 'M':
        contadorMujeres += 1
#impresion de los resultados
print(f"Hombres: {contadorHombres}, Mujeres: {contadorMujeres}")
