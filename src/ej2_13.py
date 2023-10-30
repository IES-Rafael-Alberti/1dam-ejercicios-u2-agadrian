'''
Ejercicio 2.2.3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
from ej2_04 import introducirNum


def numerosImpares(num):
    '''
    Almacena en una lista  los numeros impares desde 1 hasta el parametro introducido

    Retorna:    
            Str de los valores de la lista
    '''
    impares = []

    for i in range(1, num+1):
        if i % 2 != 0:
            impares.append(str(i))
    return impares

def main():
    print("Introudce numero: ")
    num = introducirNum()

    print(", ".join(numerosImpares(num)))



if __name__ == "__main__":
    main()