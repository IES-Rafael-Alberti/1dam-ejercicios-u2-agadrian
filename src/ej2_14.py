'''
Ejercicio 2.2.4

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

from ej2_04 import pedirNumEntero






def main():
    numero = pedirNumEntero()
    while numero < 0:
        print("Debe ser un entero positivo: ")
        numero = int(input())
    
    for i in range (numero, -1, -1):
        if i == 0:
            print(i)
        else:
            print(i, end=",")





if __name__ == "__main__":
    main()