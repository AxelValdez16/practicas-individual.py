# axel sebastian valdez lopez
# Programa para calcular el promedio de 3 calificaciones

# Pedimos las calificaciones
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

# Calculamos el promedio
promedio = (cal1 + cal2 + cal3) / 3

print("El promedio es:", promedio)

# Usamos if y else para evaluar el resultado
if promedio >= 6:
    print("¡Felicidades! Aprobaste.")
else:
    print("Lo siento, no aprobaste.")