'''
Ejercicio 2.2.19
Mostrar un menú con tres opciones:

MENÚ
----
1 - Introduzca una nota
2 - Imprimir listado
3 - Finalizar programa
Seleccione una opción => 

A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3).
Si elige una opción incorrecta, informarle del error.
El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir.
Si elige la opción 1 debe pedir que introduzca una nota.
Si elige la opción 2 se imprimirá la lista de las notas introducidas.
Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
'''


def opcMenu():
    '''
    Muestra el menu y pide por consola un numero de la opcion elegida

    Retorna: 
            int, de la opcion
    '''
    opc = input("\nMENÚ \n---- \n1 - Introduzca una nota \n2 - Imprimir listado \n3 - Finalizar programa \nSeleccione una opcion => \n\n")

    while not opc.isdigit() or int(opc) not in [1,2,3]:
        print("\nERROR - Debe elegir una de las opciones del menu: ")
        opc = input("\nMENÚ \n---- \n1 - Introduzca una nota \n2 - Imprimir listado \n3 - Finalizar programa \nSeleccione una opcion => \n\n")

    return int(opc)



def introducirNota(notas):
    '''
    Pide y almacena en una lista las notas introducidas

    No retorna nada
    '''
    nota = input("Introduce tu nota: \n")
    notas.append(nota)

    print(f"\nSe ha introducido la nota {nota}.")

    



def listaNotas(notas):
    '''
    Usando el parametro notas, imprime si hay las notas de la lista

    No retorna nada

    '''
    if not notas:
        print("\nNo hay ninguna nota añadida a la lista.")
    else:
        print("\nLista de notas: ")
        for i in notas:
            print(f"- {i}")

    

def main():
    notas = []
    
    while True:
        opc = opcMenu()
        if opc == 1:
            introducirNota(notas)
        elif opc == 2:
            listaNotas(notas)
        else:
            break


   
if __name__ == "__main__":
    main()