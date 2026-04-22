# axel sebastian valdez lopez
# Programa con funciones

# Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un círculo
def area_circulo(radio):
    import math
    return math.pi * (radio ** 2)

# Programa principal
print("Cálculo de áreas usando funciones")

# Usamos la función del rectángulo
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))
print("El área del rectángulo es:", area_rectangulo(base, altura))

# Usamos la función del círculo
radio = float(input("Ingresa el radio del círculo: "))
print("El área del círculo es:", area_circulo(radio))