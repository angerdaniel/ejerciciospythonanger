#ejercio3
# defenir la varibale de la suma de calificacioens
sumaCalificaciones = 0
#
calificacionAlta = -float('inf') #inf significa (infinito) ya que es una abreviatura y es un concepto especial utilizado
                                #para denotar un valor que es más grande que cualquier otro número posible.
                                #  Python lo utiliza principalmente en contextos matemáticos, como límites, cálculos y comparaciones.
                                #en este caso se utiliza de comparacion para aseguramos de que cualquier número ingresado 
                                # será considerado como la nueva calificación más alta o mas baja
calificacionBaja = float('inf')
#
for i in range(20):
    calificacionIngresada = float(input("Ingrese la calificación del alumno: "))
    sumaCalificaciones += calificacionIngresada
    
    if calificacionIngresada > calificacionAlta:
        calificacionAlta = calificacionIngresada
    
    if calificacionIngresada < calificacionBaja:
        calificacionBaja = calificacionIngresada

promedioCalificaciones = sumaCalificaciones / 20
#
print(f"Promedio: {promedioCalificaciones:.2f}, Calificación más alta: {calificacionAlta}, Calificación más baja: {calificacionBaja}")
