'''
Ejercicio 2.2.7

Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
from ej2_04 import introducirNum

def tablaDiez(num):
    '''
    Calcula la tabla de multiplicar de el numero introducido como parametro

    Retorna:
            str: cadena de caracteres de la tabla
    '''

    cont = 1
    tabla = ''
    for i in range(10):
        tabla += "\n" + str(num) + " x " + str(cont) + " = " + str(num*cont) 
        cont +=1
    return tabla



def main():
    print("Introduce numero de la tabla que quieres calcular: ")
    num = introducirNum()

    print(tablaDiez(num))


if __name__ == "__main__":
    main()