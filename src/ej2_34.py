'''
Ejercicio 2.2.24

Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.'''

from ej2_03 import introducirNum
from ej2_20 import comprobarPrimo

def main():
    cont_primos = 0
    while True:
        print("Introducir numero mayor a 1 (0 para terminar): ")
        num = introducirNum()

        if num == 0:
            break
        
        if comprobarPrimo(num) == True:
            cont_primos += 1
    
    print(f"Numeros primos ingresados: {cont_primos}")



if __name__ == "__main__":
    main()