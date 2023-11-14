'''
Ejercicio 2.1.9

Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''

from src.ej2_01 import pedirEdad


def precioAcceso(edad):
    '''
    Calcula el precio a pagar para entrar a la sala dependiendo de el parametro edad

    Retorna:
            int del precio de la entrada a la sala
    '''

    if edad < 4:
        return 0
    elif edad >= 4 and edad <= 18:
        return 5
    else:
        return 10
    

def main():
    precio = precioAcceso(pedirEdad())
    print(f"El precio de tu entrada es de {precio}€")


if __name__ == "__main__":
    main()
