'''
Ejercicio 2.1.3

Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

def introducirNum():
    '''
    Almacena numero introducido. Si no introduce un numero o es negativo, da error y vuelve a pedirlo

    Retorna: 
            - Int: si introduce un int
            - Float: si introduce un float
    '''
    num = input("")

    while type(num) != int and type(num) != float:
        if num.isdigit():
            return int(num)
        elif num.replace(".","",1).isdigit():
            return float(num)
        else:
            print("ERROR - Solo se pueden introducir numeros positivos")
            num = input("")


def dividirNumeros(num1 , num2):
    '''
    Divide los dos numeros que se le pasa por parametro. Si el num2 = 0, da error

    Retorna: float del resultado
    '''
    resultado = 0

    if num2 == 0:
        print("Error - El divisor no puede ser 0.")
        return None

    else:
        resultado = num1/num2

    return float(resultado)


def main():
    print("Introduce un numero")
    num1 = introducirNum()

    print("Introduce otro numero")
    num2 = introducirNum()
    
    resultado = dividirNumeros(num1, num2)
    if num2 != 0:
        print(f"El resultado de {num1} / {num2} = {resultado}")
   

if __name__ == "__main__":
    main()