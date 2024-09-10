# Ejercicio 9
#las variables de los contadores y sumas de edades para hombres y mujeres
contadorHombres = 0
contadorMujeres = 0
sumaEdadesHombres = 0
sumaEdadesMujeres = 0
cantidadAlumnos = int(input("Ingrese la cantidad total de alumnos: "))
#bucle para leer los datos de los almunos 
for i in range(cantidadAlumnos):
    sexoAlumno = input("Ingrese el sexo del alumno (H/M): ").upper()
    edadAlumno = int(input("Ingrese la edad del alumno: "))
    
    if sexoAlumno == 'H':
        contadorHombres += 1
        sumaEdadesHombres += edadAlumno
    elif sexoAlumno == 'M':
        contadorMujeres += 1
        sumaEdadesMujeres += edadAlumno

# Cálculo de promedios utilizando estructuras condicionales tradicionales
if contadorHombres > 0:
    promedioEdadHombres = sumaEdadesHombres / contadorHombres
else:
    promedioEdadHombres = 0

if contadorMujeres > 0:
    promedioEdadMujeres = sumaEdadesMujeres / contadorMujeres
else:
    promedioEdadMujeres = 0

if cantidadAlumnos > 0:
    promedioEdadGrupo = (sumaEdadesHombres + sumaEdadesMujeres) / cantidadAlumnos
else:
    promedioEdadGrupo = 0

# Imprimir los resultados
print(f"Promedio de edad por grupo:")
print(f"Hombres: {promedioEdadHombres:.2f} años")
print(f"Mujeres: {promedioEdadMujeres:.2f} años")
print(f"Grupo total: {promedioEdadGrupo:.2f} años")
