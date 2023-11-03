'''
Ejercicio 2.2.25

Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más
'''

from ej2_06 import pedirTexto


def dividirFrase(frase):
    '''
    Divide la frase en palabras, calcula la longitud de cada una y almacena la mas larga y el numero total de palabras

    Retorna:
            str: de la plabra mas larga
            str: de la cantidad de palabras
    '''
    palabras = frase.split(" ")
    cantPalabras = len(palabras)
    masLarga = max(palabras, key=len)

    return masLarga, cantPalabras


def main():
    print("Introduce frase: ")
    frase = pedirTexto()

    masLarga, cantPalabras = dividirFrase(frase)

    print(f"La palabra mas larga es: {masLarga}. Palabras totales: {cantPalabras}")


if __name__ == "__main__":
    main()