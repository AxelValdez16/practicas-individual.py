# axel sebastian valdez lopez
# Programa que usa listas

# Creamos una lista de frutas
frutas = ["manzana", "plátano", "naranja", "uva"]

# Recorremos la lista con un ciclo for
print("Lista de frutas:")
for fruta in frutas:
    print(fruta)

# Accedemos a un elemento por índice
print("\nLa primera fruta es:", frutas[0])

# Agregamos una nueva fruta
frutas.append("mango")
print("Lista después de agregar mango:", frutas)

# Eliminamos una fruta
frutas.remove("plátano")
print("Lista después de eliminar plátano:", frutas)