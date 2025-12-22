# Cometnario de una linea
"""
Comentario de varias lineas

ESTE ES MI PRIMER ARCHIVO DE PYTHON
"""
comentario = "Comentario de una linea"
condicional = (16 > 10) and (16 < 20)

if (condicional and comentario): 
    print("Verdadero")
elif (condicional or comentario):
    print("Verdadero a medias")
else:
    print("Falso")


print("---------------- BUCLE FOR ----------------")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

print("---------------- BUCLE WHILE ----------------")
i = 0
while i <= 5:
    print(i)
    i += 1



"""
Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista. Algunos métodos comunes son:

    append(elemento): agrega un elemento al final de la lista.
    insert(indice, elemento): inserta un elemento en una posición específica de la lista.
    remove(elemento): elimina la primera aparición de un elemento en la lista.
    pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
    sort(): ordena los elementos de la lista en orden ascendente.
    reverse(): invierte el orden de los elementos en la lista.

"""

juanito = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Madrid"
}

juanito.update({"edad": 21})

print(juanito)



conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}


frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()