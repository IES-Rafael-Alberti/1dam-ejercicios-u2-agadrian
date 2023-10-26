'''
Ejercicio 2.1.5

Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''

def pedirNumero():
    '''
    Pide un numero por consola

    Retorna: int
    '''
    num = int(input())

    return num


def main():
    print("Introduce tu edad: ")
    edad = pedirNumero()
    print("Introduce tus ingeresos: ")
    ingresos = float(pedirNumero())

    if (edad > 16) and (ingresos >= 1000):
        print("Debes tributar")
    else:
        print("No tienes porque tributar")
    

    

if __name__ == "__main__":
    main()