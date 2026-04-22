# Programa para calcular el precio con descuento

precio = float(input("Ingresa el precio original: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

# Calculamos el monto del descuento
monto_descuento = precio * (descuento / 100)

# Calculamos el precio final
precio_final = precio - monto_descuento

print("El descuento es de:", monto_descuento)
print("El precio final a pagar es:", precio_final)

# Usamos if y else para dar un mensaje adicional
if descuento > 0:
    print("Se aplicó un descuento.")
else:
    print("No se aplicó ningún descuento.")