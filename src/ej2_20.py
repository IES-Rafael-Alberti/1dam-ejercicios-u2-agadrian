'''
Ejercicio 2.2.10

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.'''


from ej2_04 import introducirIntPositivo

def comprobarPrimo(numero):
    '''
    Comprueba si el numero pasado por paramtero es primo o no

    Retorna:
        True si lo es
        False si no
    '''
    
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        # Comprobar si es divisible por números impares desde 3 hasta la raíz cuadrada de numero
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True


def main():
    print("Introduce numero a comprobar si es primo: ")
    numero = introducirIntPositivo()

    if comprobarPrimo(numero) == True:
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    main()