'''
Ejercicio 2.2.5

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
    amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
'''



def introducirNum():
    '''
    Almacena numero introducido. Si no introduce un numero, da error y vuelve a pedirlo

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
            print("ERROR - Solo se pueden introducir numeros")
            num = input("")
        


  


def main():
    print("Introduce cantidad a invertir: ")
    inversion = introducirNum()
    
    print("Introduce interes anual: ")
    interes = introducirNum()

    print("Introduce numero de años: ")
    años = introducirNum()

    capital = inversion * años + (interes / 100)

    print(f"Tu capital final obtenido sera de {capital} €. Equivale a {capital / años}€ anuales.")

if __name__ == "__main__":
    main()