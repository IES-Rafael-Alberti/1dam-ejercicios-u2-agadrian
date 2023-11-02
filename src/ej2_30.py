'''
Ejercicio 2.2.20

Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.'''

from ej2_06 import pedirTexto



def buscarLetra(frase,letra):
    indice = 0
    pos = ""
    frase = frase.replace(" ", "")

    for i in frase:
        if i == letra:
            pos += "\nHay coincidencia en la posicion " + str(indice)
            break
        else:
            print("No hay coincidencia en la posicion: " + str(indice))
        indice += 1
    print(pos)
    return pos





def main():
    print("Introduce frase: ")
    frase = pedirTexto()

    print("Introduce letra: ")
    letra = pedirTexto()

    buscarLetra(frase,letra)



if __name__ == "__main__":
    main()