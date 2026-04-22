# axel sebastian valdez lopez
# Arreglos con listas de Python
numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)

# Acceder a elementos
print("Primer elemento:", numeros[0])
print("Último elemento:", numeros[-1])

# Modificar un valor
numeros[2] = 99
print("Lista modificada:", numeros)

# Recorrer el arreglo
for n in numeros:
    print("Elemento:", n)

# -----------------------------
# Arreglos con NumPy
import numpy as np

# Crear un arreglo NumPy
arr = np.array([1, 2, 3, 4, 5])
print("Arreglo NumPy:", arr)

# Operaciones matemáticas rápidas
print("Arreglo + 10:", arr + 10)
print("Arreglo * 2:", arr * 2)

# Arreglo multidimensional (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", matriz)

# Suma de todos los elementos
print("Suma total:", np.sum(matriz))

# Transpuesta de la matriz
print("Transpuesta:\n", matriz.T)