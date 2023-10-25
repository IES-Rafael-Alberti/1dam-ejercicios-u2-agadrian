'''
Ejercicio 2.1.3

Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

def pedirNum():
    '''
    Pide por consola un numero

    Retorna: float del numero introducido
    '''
    numero = float(input("Introduce un numero: \n"))

    return numero


def dividirNumeros(num1 , num2):
    '''
    Divide los dos numeros que se le pasa por parametro. Si el num2 = 0, da error

    Retorna: float si num2 = 0.   Str si num2 != 0
    '''

    if num2 == 0:
        resultado = "Error - El divisor no puede ser 0."
    else:
        resultado = num1 / num2

    return resultado


def main():
    num1 = pedirNum()
    num2 = pedirNum()
    
    print(dividirNumeros(num1, num2))
   

if __name__ == "__main__":
    main()