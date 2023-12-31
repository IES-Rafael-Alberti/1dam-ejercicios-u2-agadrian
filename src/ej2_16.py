'''
Ejercicio 2.2.6

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****

'''

from ej2_04 import introducirIntPositivo


def crearTriangulo(altura):
    '''
    Crea un triangulo usano * de la altura introducida en el parametro, y lo almacena en variable

    Retorna:
            Str: cadena de caracteres de la variable 
    '''
    arbol = ''
    cont = 1
    for i in range(altura):
        arbol += ("*" * cont) + "\n"
        cont += 1
    return arbol


def main():
    print("Introduce la altura de el triangulo: ")
    altura = introducirIntPositivo()
    print(crearTriangulo(altura))


if __name__ == "__main__":
    main()