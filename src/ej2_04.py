'''
Ejercicio 2.1.4

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

def pedirNumEntero():
    '''
    Pide por consola un numero entero

    Retorna: int
    '''
    numero = int(input("Introduce un numero entero: \n"))

    return numero



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
    if comprobarPar(pedirNumEntero()):
        print("El numero es par")
    else:
        print("El numero es impar")
   

if __name__ == "__main__":
    main()