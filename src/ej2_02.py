'''
Ejercicio 2.1.2

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

def comprobarContraseña(contraseña, contraseña2):
    """
    Comprueba que las contraseñas coincidan

    Retorna
    -------
    Boolean
            True si coinciden
            False si no coinciden
    """
    if (contraseña.lower()) == (contraseña2.lower()):
        return True
    else:
        return False
    
    

def main():
    contraseña = "p4ssw0rd"
    contraseña2 = input("Introduce contraseña: \n")

    if comprobarContraseña(contraseña,contraseña2):
        print("Las contraseñas coinciden")
    else:
        print("Las contraseñas no coinciden")
    



if __name__ == "__main__":
    main()
