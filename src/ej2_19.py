'''
Ejercicio 2.2.9

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''


def comprobarContraseña(password, password2):
    '''
    Comprueba si los dos parametros introducidos son iguales

    Retorna:
            True si son iguales
            False si no son iguales
    '''
    if password == password2:
        return True
    else:
        return False



def main():
    password =  "KHVGhgjbby68ygb"
    password2 = input("Introduce contraseña: ")

    while comprobarContraseña(password, password2) == False:
        password2 = input("Contraseña incorrecta, introduce contraseña: ")
    print("Contraseña correcta!!")


if __name__ == "__main__":
    main()