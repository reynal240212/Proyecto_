# Solicitud de información
Nombre_completo = input(f"Ingresa tu nombre completo: ")
materias = 5
# Asignación de variables
CONTADOR = 1
sumatoria = 0
# Ciclo
while CONTADOR <= materias:
  nombre_materia = input(f"Ingrese el nombre de la materia {CONTADOR}: ") # Pedir nombre de la materia
  calificacion = float(input(f"Ingrese la calificación de {nombre_materia}: ")) # Pedir calificación de la materia
# Sumatoria
  sumatoria = sumatoria + calificacion
# Aumentar el contador para cerrar el ciclo
  CONTADOR = CONTADOR + 1
# Cálculos
Promedio = sumatoria / materias
# Imprimir resultados
print (f"Nombre: ", Nombre_completo)
print (f"Promedio: ", Promedio)
