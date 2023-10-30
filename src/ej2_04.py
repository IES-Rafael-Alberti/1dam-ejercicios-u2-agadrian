'''
Ejercicio 2.1.4

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

from ej2_03 import introducirNum


def comprobarPar(num):
    '''
    Comprueba si un numero es par o no

    Retorna - boolean: True or False
    '''
    if (num % 2) == 0:
        return True
    else: 
        return False


def main():
    print("Introduce un numero: ")
    num = introducirNum()
    if comprobarPar(num):
        print("El numero es par")
    else:
        print("El numero es impar")
   

if __name__ == "__main__":
    main()