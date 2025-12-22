def saludar(nombre):
    print(f"Hola {nombre} desde python")
nombre = input("Introduzca el nombre de quien quiera saludar: ")
saludar(nombre)


def comprobarEdad (edad): 
    if edad <18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
edad = int(input("Introduzca su edad: "))
comprobarEdad(edad)