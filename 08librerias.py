# axel sebastian valdez lopez
# Librerías estándar
import math
import random
import datetime

# Librerías externas (se instalan con pip)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ejemplo de uso
print("Número pi:", math.pi)

# Número aleatorio entre 1 y 10
print("Aleatorio:", random.randint(1, 10))

# Fecha actual
print("Hoy es:", datetime.date.today())

# Crear un arreglo con NumPy
arr = np.array([1, 2, 3, 4, 5])
print("Arreglo NumPy:", arr)

# Crear un DataFrame con Pandas
data = {"Nombre": ["Ana", "Luis", "María"], "Edad": [18, 20, 22]}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Gráfico con Matplotlib
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Ejemplo de gráfico")
plt.show()