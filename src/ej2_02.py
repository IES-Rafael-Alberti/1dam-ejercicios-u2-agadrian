'''
Ejercicio 2.1.2

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

def pedirContraseña():
    """
    Pedir que introduzca una contraseña

    Retorna
    -------
    Str: cadena de caracteres introducidos
    """
    
    contraseña = input("Introduce contraseña: \n")

    return contraseña



def main():
    contraseña = "p4ssw0rd"
    contraseña2 = pedirContraseña()

    if (contraseña.lower()) == (contraseña2.lower()):
        print("Las contraeñas son iguales.")
    else:
        print("Las contraseñas no coinciden")



if __name__ == "__main__":
    main()
