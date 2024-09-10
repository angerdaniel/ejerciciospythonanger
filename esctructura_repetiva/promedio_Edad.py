# Ejercicio 5
#la variable de contadores de grupo edad y sumas los pesos
contadorNiños = contadorJovenes = contadorAdultos = contadorAncianos = 0
sumaPesoNiños = sumaPesoJovenes = sumaPesoAdultos = sumaPesoAncianos = 0

# El bucle es Simulación de la entrada de datos para 50 personas
for i in range(50):
    edadPersona = int(input("Ingrese la edad de la persona: "))
    pesoPersona = float(input("Ingrese el peso de la persona (kg): "))
    
    if edadPersona <= 12:
        contadorNiños += 1
        sumaPesoNiños += pesoPersona
    elif edadPersona <= 29:
        contadorJovenes += 1
        sumaPesoJovenes += pesoPersona
    elif edadPersona <= 59:
        contadorAdultos += 1
        sumaPesoAdultos += pesoPersona
    else:
        contadorAncianos += 1
        sumaPesoAncianos += pesoPersona

# Cálculo de promedios 
if contadorNiños > 0:
    promedioPesoNiños = sumaPesoNiños / contadorNiños
else:
    promedioPesoNiños = 0

if contadorJovenes > 0:
    promedioPesoJovenes = sumaPesoJovenes / contadorJovenes
else:
    promedioPesoJovenes = 0

if contadorAdultos > 0:
    promedioPesoAdultos = sumaPesoAdultos / contadorAdultos
else:
    promedioPesoAdultos = 0

if contadorAncianos > 0:
    promedioPesoAncianos = sumaPesoAncianos / contadorAncianos
else:
    promedioPesoAncianos = 0

# Imprimir los resultados
print(f"Promedio de peso por categorías de edad:")
print(f"Niños: {promedioPesoNiños:.2f} kg")
print(f"Jóvenes: {promedioPesoJovenes:.2f} kg")
print(f"Adultos: {promedioPesoAdultos:.2f} kg")
print(f"Ancianos: {promedioPesoAncianos:.2f} kg")
