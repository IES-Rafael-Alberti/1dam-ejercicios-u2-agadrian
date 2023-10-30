'''
Ejercicio 2.2.3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''
from ej2_04 import pedirNumEntero



def main():
    num = pedirNumEntero()
    impares = []
    for i in range(1, num+1):
        if i % 2 != 0:
            impares.append(str(i))
            #print(i, ",".join(""))

    print(", ".join(impares))

if __name__ == "__main__":
    main()