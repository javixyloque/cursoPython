# FUNCIONES LAMBDA  (FUNCIONES ANONIMAS)
cuadrado = lambda x: x ** 2
print("CUADRADO DE 5 FUNCIÓN LAMBDA: ",cuadrado(5), "\n")

# FUNCIONES MAP (EN UNA LISTA PORQUE UNA TUPLA NO SE PUEDE MODIFICAR)
numeros = [1, 2, 3, 4, 5]
doble = list(map(lambda x: x * 2, numeros))
print("CÁLCULO DE DOBLES DE NUMEROS EN TUPLA: ", doble, "\n")

# ARGS PARA AÑADIR NUMERO INDETERMINADO DE PARAMETROS (CALCULAR MEDIA)
numerosMedia = [192, 543, 35, 462]
def media (*numeros) : 
    return float(sum(numeros) / len(numeros))

print("MEDIA NUMEROS EN LA LISTA: ",media(*numerosMedia))
print("MEDIA DE PARÁMETROS PASADOS: ",media(192, 543, 35, 25, 23), "\n")



# COMENTARIOS DE FUNCIONES

def area_rectangulo(base, altura):
    """
    _Calcula el **área** de un rectángulo_.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

# print(area_rectangulo.__doc__)
print("ÁREA DE RECTÁNGULO BASE 5 Y ALTURA 10: ",area_rectangulo(5, 10), "\n")

print("TAMBIEN HAY CONTEXTO EN LAS VARIABLES, LOCALES Y GLOBALES")