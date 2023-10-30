'''
Ejercicio 2.1.5

Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''
from ej2_03 import introducirNum

def comprobarTributacion(edad,ingresos):
    '''
    Se le pasa los parametros y comprueba si ha de tributar o no

    Retorna:
            Boolean
                    True: si debe de tributar
                    False: si no debe de tributar
    '''
    if (edad > 16) and (ingresos >= 1000):
        return True
    else:
        return False


def main():
    print("Introduce tu edad: ")
    edad = introducirNum()

    print("Introduce tus ingeresos: ")
    ingresos = introducirNum()

    if comprobarTributacion(edad,ingresos):
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")


    
    

    

if __name__ == "__main__":
    main()