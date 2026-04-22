# Axel Sebastian Valdez Lopez
# Ejemplo de operadores lógicos en Python

a = True
b = False

# AND: devuelve True si ambas condiciones son verdaderas
resultado_and = a and b   # False

# OR: devuelve True si al menos una condición es verdadera
resultado_or = a or b     # True

# NOT: invierte el valor lógico
resultado_not = not a     # False

print("a AND b =", resultado_and)
print("a OR b =", resultado_or)
print("NOT a =", resultado_not)

# Ejemplo práctico
edad = 16
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Puedes entrar.")
elif edad >= 18 or tiene_permiso:
    print("Puedes entrar con condiciones.")
else:
    print("No puedes entrar.")
