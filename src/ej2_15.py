'''
Ejercicio 2.2.5

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
    amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 
'''


from ej2_04 import introducirNum

  


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