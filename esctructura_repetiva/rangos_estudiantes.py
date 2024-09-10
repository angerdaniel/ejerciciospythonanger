# Ejercicio 8
#variable de los contadores para cada rango de calificaciones
contadorMenor50 = 0
contadorEntre50y69 = 0
contadorEntre70y79 = 0
contadorMayor80 = 0
# Bucle for para leer las calificaciones de 23 estudiantes
for i in range(23):
    calificacionEstudiante = float(input("Ingrese la calificación del estudiante (1-100): "))
    
    if calificacionEstudiante < 50:
        contadorMenor50 += 1
    elif 50 <= calificacionEstudiante < 70:
        contadorEntre50y69 += 1
    elif 70 <= calificacionEstudiante < 80:
        contadorEntre70y79 += 1
    else:
        contadorMayor80 += 1
#impresion de los resultados
print(f"Menor a 50: {contadorMenor50}, Entre 50 y 69: {contadorEntre50y69}, Entre 70 y 79: {contadorEntre70y79}, Mayor o igual a 80: {contadorMayor80}")
