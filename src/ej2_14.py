'''
Ejercicio 2.2.4

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

from ej2_04 import introducirIntPositivo


def cuentaAtras(numero):
    '''
    Almacena en una lista la cuenta atras desde el parametro introducido hasta 0

    Retorna:
            Str de los valores de la lista separados por comas
    '''

    lista = []
    
    for i in range (numero, -1, -1):
        lista.append(str(i))
    return lista
        


def main():
    print("Introduce numero: ")
    numero = introducirIntPositivo()

    print(", ".join(cuentaAtras(numero)))


if __name__ == "__main__":
    main()