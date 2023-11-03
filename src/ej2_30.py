'''
Ejercicio 2.2.20

Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.'''

from ej2_06 import pedirTexto



def buscarLetra(frase,letra):
    '''
    Se le pasa una frase y una letra como parametro. Busca si la letra está en la frase

    Retorna:
            str, del mensaje que informa si esta o no
    '''
    indice = 0
    pos = ""
    frase = frase.replace(" ", "")

    for i in frase:
        if i == letra:
            pos += "Hay coincidencia en la posicion: " + str(indice) + " --> " + str(i) + "\nFinalizando..."
            
            break
        else:
            pos +="No hay coincidencia en la posicion: " + str(indice) + " --> " + str(i) + "\n"
            
        indice += 1
    
    return pos





def main():
    print("Introduce frase: ")
    frase = pedirTexto()

    print("Introduce letra: ")
    letra = pedirTexto()

    print(buscarLetra(frase,letra))



if __name__ == "__main__":
    main()