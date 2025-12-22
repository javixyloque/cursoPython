import sys
# "r" ES EL MODO DE LECTURA
try:
    # DESDE LA CARPETA EN LA QUE SE EJECUTA LA TERMINAL

    archivo = open("./apuntesPython/datos.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")

contenido = archivo.read()
print(contenido)
archivo.close()

try:
    archivo = open("nuevoArchivo.txt", "a")
    archivo.write("\nContinuando prueba")
    archivo.close()
except FileNotFoundError:
    print("Error: Archivo no encontrado")


# MANEJAR APERTURA Y CIERRE AUTOMÁTICO
with open("apuntesPython/datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)