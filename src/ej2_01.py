"""
Ejercicio 2.1.1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

def pedirEdad():
    """
    Pedir la edad y comprobar que se trata de un número entero entre 1 y 125.
    
    Retorna
    -------
    int
        un entero con el valor de la edad introducida por consola.
    """
    salir = False
    while not salir:
        entrada = input("Introduzca su edad: ")

        if entrada.isnumeric() and 0 < int(entrada) <= 125:
            salir = True
        else:
            print("***Error*** edad introducida no válida.")
    
    edad = int(entrada)

    return edad


def mayorEdad(edad):
    """
    Comprobar si la edad corresponde a una persona mayor de edad o no.
    
    Retorna
    -------
    bool
        True es mayor de edad / False no es mayor de edad.
    """
    if edad >= 18:
        return True
    else:
        return False
    

def main():
    edad = pedirEdad()

    if mayorEdad(edad):
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")


if __name__ == "__main__":
    main()
