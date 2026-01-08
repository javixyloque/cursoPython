def filter_list(l):
    """
    In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
    """
    lista_devuelta = []
    for elemento in l:
        if isinstance(elemento, int):
            if (elemento >= 0):
                lista_devuelta.append(elemento)
    return lista_devuelta


import math

def is_square(n):
    """
    In this kata you have to return true if a number given is the square of another integer or false if it's not
    """
    if (n < 0):
        return False
    raiz = (math.sqrt(n))
    num_entero = math.ceil(raiz)
    print(raiz, num_entero)
    if raiz != num_entero:
        return False
    else:
        return True
    



def high_and_low (numbers):
    """
    In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
    """
    array_numeros = numbers.split(" ")
    array_enteros = []
    for num in array_numeros:
        array_enteros.append(int(num))
    array_ordenados = sorted(array_enteros)
    return str(array_ordenados[-1])+" "+str(array_ordenados[0])
    

def howManyInTheBus(bus_stops):
    """
    https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
    """
    pasajeros = 0
    for parada in bus_stops:
        pasajeros+=parada[0]; pasajeros-=parada[1]

    if pasajeros >=0:
        return pasajeros
    else:
        return 0



def find_short(s):
    """
    Simple, given a string of words, return the length of the shortest word(s).
    String will never be empty and you do not need to account for different data types.
    """
    array_caracteres = s.split(" ")
    
    array_longitudes = []
    for palabra in array_caracteres:
        array_longitudes.append(len(palabra))
    array_ordenado = sorted(array_longitudes)
    return int(array_ordenado[0])

