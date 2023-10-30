'''
Ejercicio 2.2.2

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
from ej2_01 import pedirEdad



def main():
    edad = pedirEdad()
    
    for i in  range (1,edad+1):
        if i == 1:
            print(f"Has cumplido {i} año!")
        else:
            print(f"Has cumplido {i} años!")
    pass



if __name__ == "__main__":
    main()