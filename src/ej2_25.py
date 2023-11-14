'''
Ejercicio 2.2.15

Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
'''
from ej2_04 import introducirIntPositivo

def sumatoriaIntsPositivos():
    '''
    Pide numeros enteros positivos y los va sumando. Cuando introduce el 0 se acaba

    Retorna: str de la lista de numeros introducidos y el rsultado de sumarlos
    '''
    print("Introduce un entero positivo (0 para salir): ")
    num = introducirIntPositivo()

    suma = 0
    lista = '' +  str(num)

    while num != 0:
        suma += num
        print("Introduce otro entero positivo (0 para salir): ")
        num = introducirIntPositivo()

        if num  != 0:
            lista += " + " + str(num)
        else:
            lista += " = " + str(suma)

    print("Adiós!")

    return lista


def  main():
    resultado = sumatoriaIntsPositivos()
    print(resultado)



if __name__ == "__main__":
    main()