# IMPORTAR LIBRERIA COMPLETA (MÓDULO)
import math
print(math.sqrt(9))

# IMPORTAR FUNCIÓN ESPECÍFICA DE UNA LIBRERÍA
from math import sqrt
print(sqrt(9))





# OTROS EJEMPLOS DE BIBLIOTECAS (MÓDULOS MUY COMUNES)

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual
