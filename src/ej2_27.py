'''
Ejercicio 2.2.17

Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
'''

from ej2_04 import introducirIntPositivo


def sumaDigitos(num):
    '''
    Separa y suma cada digito de un numero introducido como parametro

    Retorna: int de la suma
    '''
    suma = 0

    while num != 0:
        #obtiene el ultimo digito del numero
        lastNum = num % 10 

        suma += lastNum

        #elimina el ultimo digito del numero
        num = num //10 
    return suma


def  main():
    print("Introduce un numero entero positivo: ")
    num = introducirIntPositivo()

    suma = sumaDigitos(num)
    print(f"La suma de los digitos que componen {num} es: {suma}.")


if __name__ == "__main__":
    main()