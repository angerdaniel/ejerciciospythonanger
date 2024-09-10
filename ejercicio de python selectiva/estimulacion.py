# La variable para ingresar el promedio de notas del estudiante
promedioAlumnos = float(input("Notas del estudiante: "))

# La variable para ingresar cuánto le cobran de la pensión
pensionBase = float(input("Pensión sin IVA: "))

# Definir la variable para obtener el resultado de la pensión a pagar
if promedioAlumnos >= 4.0:    
    plataPagar = pensionBase * 0.7
else:
    plataPagar = pensionBase * 1.1

# La impresión de datos del promedio de notas y la pensión que debe pagar el estudiante
print(f"El alumno aprobó con un promedio de: {promedioAlumnos} y debería pagar: ${plataPagar:.2f}")
