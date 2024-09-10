# Variables para obtener los datos del usuario
nombreDelEstudiante = input("Escriba el nombre del estudiante: ")
actividadesPromedio = float(input("La calificación de las actividades: "))
proyectoFinal = float(input("La calificación del proyecto final: "))
parcialesPromedio = float(input("La calificación de las parciales: "))

# Variable para calcular el valor de la calificación final
notaFinal = (actividadesPromedio * 0.30) + (proyectoFinal * 0.50) + (parcialesPromedio * 0.20)

# Impresión de la calificación y evaluación
if notaFinal >= 70:
    print(f"{nombreDelEstudiante}, su promedio es {notaFinal:.1f}, su calificación es aceptable.")
else:
    print(f"{nombreDelEstudiante}, su promedio es {notaFinal:.1f}, su calificación es reprobó.")
