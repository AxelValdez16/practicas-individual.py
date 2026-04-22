# axel sebastian valdez lopez
# Ejemplo de manejo de errores

try:
    # Intentamos dividir entre cero (esto genera un error)
    resultado = 10 / 0
    print("Resultado:", resultado)

except ZeroDivisionError:
    # Capturamos el error específico
    print("Error: No se puede dividir entre cero.")

except Exception as e:
    # Captura cualquier otro error inesperado
    print("Ocurrió un error inesperado:", e)

else:
    # Se ejecuta solo si no hubo errores
    print("La operación fue exitosa.")

finally:
    # Se ejecuta siempre, haya o no error
    print("Fin del bloque try-except.")