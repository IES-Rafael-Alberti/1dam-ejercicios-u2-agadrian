'''
Ejercicio 2.2.14

Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
'''

def introducirInt():
    '''
    Si no introduce un entero, vuelve a pedirlo

    Retorna: int
    '''
    num = input()

    while type(num) != int:
        if num.isdigit() or num.replace("-", "").isdigit():
            return int(num)
        else:
            print("Solo puedes introducir un numero entero: ")
            num = input()
        

def sumatoriaInts():
    '''
    Pide numeros enteros y los va sumando. Cuando introduce el 0 se acaba

    Retorna: str de la lista de numeros introducidos y el rsultado de sumarlos
    '''
    print("Introduce un entero (0 para salir): ")
    num = introducirInt()

    suma = 0
    lista = '' +  str(num)

    while num != 0:
        suma += num
        print("Introduce otro entero (0 para salir): ")
        num = introducirInt()

        if num  != 0:
            lista += " + " + str(num)
        else:
            lista += " = " + str(suma)

    print("Adiós!")

    return lista


def  main():
    resultado = sumatoriaInts()
    print(resultado)


if __name__ == "__main__":
    main()