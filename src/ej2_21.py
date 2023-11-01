'''
Ejercicio 2.2.11

Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

from ej2_06 import pedirTexto


def letrasInvertidas(palabra):
    '''
    Invierte el orden de las letras introducidas y las almacena cada una en linea diferente

    Retorna: str del contenido almacenado en la variable
    '''
    final = ''
   
    for i in palabra[::-1]:
        final += i + "\n"
    return final



def main():
    print("Introduce una palabra: ")
    palabra = pedirTexto()

    print(letrasInvertidas(palabra))



if __name__ == "__main__":
    main()