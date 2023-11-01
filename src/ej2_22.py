'''
Ejercicio 2.2.12

Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''
from ej2_06 import pedirTexto


def letrasEnFrase(frase,letra):
    '''
    Comprueba cuantas veces aparece el parametro letra en el parametro frase

    Retorna: Int del contador de veces
    '''
    cont = 0
    for i in frase:
        if i == letra:
            cont +=1
    return cont



def main():
    print("Introduce una frase: ")
    frase = pedirTexto()

    print("Introduce una letra: ")
    letra = pedirTexto()

    veces = letrasEnFrase(frase,letra)
    print(f"Veces que aparece tu letra en la frase: {veces}.")



if __name__ == "__main__":
    main()