
def smash (words):
    """
    Devuelve un string de un array pasado como parámetro con espacios
    """
    return " ".join(words)

def solution (text, ending):
    """
    Comprueba si el final del text coincide con el ending (strings)
    """
    return text.endswith(ending)

def count_bits(n):
    """
    Comprueba los bits (1) de la versión binaria de un número decimal
    """
    numBin = bin(n)
    arrayBin = list(str(numBin))
    del arrayBin[0:2]
    contador = 0
    for digito in arrayBin:
        if digito == '1':
            contador = contador + 1
    return contador



