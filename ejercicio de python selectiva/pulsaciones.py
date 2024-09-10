# Las variables para obtener los datos del usuario
nombre = input("Escriba su nombre: ")
sexo = input("Masculino o femenino: ").strip().lower()
edad = int(input("¿Cuántos años tienes?: "))

# Definir los valores de los datos de usuarios para calcular sus pulsaciones
if sexo == "masculino":
    numPulsaciones = (210 - edad) / 10
elif sexo == "femenino":
    numPulsaciones = (220 - edad) / 10

# Impresión de los datos de usuarios
print("El nombre es: {0}, el sexo es: {1}, su edad es: {2} años, y el número de sus pulsaciones es: {3:.2f}".format(nombre.capitalize(), sexo.capitalize(), edad, numPulsaciones))
