'''
Ejercicio 2.1.4

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

def introducirIntPositivo():
    '''
    Pide un valor, si es int lo almacena, y si no vuelve a pedirlo

    Retorna: int
    '''
    num = input()

    while not num.isdigit():
        print("Debe ser un numero entero positivo")
        num = input()
    return int(num)
        
   


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
    print("Introduce un numero entero: ")
    num = introducirIntPositivo()
    if comprobarPar(num):
        print("El numero es par")
    else:
        print("El numero es impar")
   

if __name__ == "__main__":
    main()