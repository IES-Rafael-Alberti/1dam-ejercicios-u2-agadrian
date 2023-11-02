'''
Ejercicio 2.2.18

Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
'''
from ej2_24 import introducirInt
from ej2_27 import sumaDigitos



def main():
    contPares = 0

    while True:
        print("Introduce numeros enteros positivos (-1 para acabar)")
        num = introducirInt()

        if num == -1:
            break

        if num < 0:
            print("Debe ser un entero positivo")
        else:
            suma = sumaDigitos(num)
            print(f"La suma de los digitos del numero introducido es: {suma}")

            if num % 2 == 0:
                contPares += 1
    print(f"Cantidad de numeros pares introducidos: {contPares}")
                
        

if __name__ == "__main__":
    main()