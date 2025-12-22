try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

archivo = None
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    if archivo: 
        archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción (aunque no se va a poder cerrar si no existe el archivo)



def funcion():
# Código que puede generar una excepción personalizada
    if 1 == 1:
        raise Exception("Como 1 es igual a 1, se triggea esta alerta de excepción")
try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    print("Fin de la script")
