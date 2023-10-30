'''
Ejercicio 2.2.2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
from ej2_01 import pedirEdad


def añosCumplidos(edad):
    '''
    Almacena en una lista los años de alguien empezando desde 1 hasta el parametro introducido

    Retorna: str de los valores de la lista
    '''
    resultado = []

    for i in range(1,edad+1):
        resultado.append(str(i))
    return resultado


def main():
    edad = pedirEdad()

    print(", ".join(añosCumplidos(edad)))
    


if __name__ == "__main__":
    main()