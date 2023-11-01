'''
Ejercicio 2.2.5

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
    amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
'''


from ej2_03 import introducirNum

  
def capitalInversion(inversion,interes,años):
    ''''
    Calcula con una formula el capital obtenido en una inversion usando los parametros, y o almacena en una variable

    Retorna:  
            Str: cadena de caracteres de el mensaje a mostrar
    '''
    inversion *=  1 + (interes / 100)
    msg = "Tu capital final obtenido sera de " + str(inversion * años) + " €. Equivale a " + str(inversion) + " € anuales."
    
    return msg

def main():
    print("Introduce cantidad a invertir: ")
    inversion = introducirNum()
    
    print("Introduce interes anual: ")
    interes = introducirNum()

    print("Introduce numero de años: ")
    años = introducirNum()

    print(capitalInversion(inversion,interes,años))

if __name__ == "__main__":
    main()