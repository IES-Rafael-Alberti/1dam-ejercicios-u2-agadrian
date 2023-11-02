'''
Ejercicio 2.2.16

Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
'''
from ej2_04 import introducirIntPositivo

def encontrarMayor():
    '''
    Pide y alamacena numero enteros positivos introducidos

    Reotrna: int, el numero mas grande
    '''

    print("Introduce un entero positivo (0 para salir): ")
    num = introducirIntPositivo()

    mayor = 0

    while num != 0:
        if num > mayor:
            mayor = num
        print("Introduce otro entero positivo (0 para salir): ")
        num = introducirIntPositivo()
        
    return mayor



def  main():
    numeroMayor = encontrarMayor()
    print(f"El numero mayor es el {numeroMayor}.")


if __name__ == "__main__":
    main()