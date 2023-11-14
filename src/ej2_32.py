'''
Ejercicio 2.2.22

Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
'''

from ej2_04 import introducirIntPositivo


def digitosParImpar(num,par,impar):
    '''
    Se le pasa por parametro el numero, y los contadores de par e impar. Depende de lo que sea, aumenta en 1 el contador

    Retorna:
            int, int de los contadores
    '''

    for i in str(num):
        
        if int(i) % 2 == 0:
            par += 1
        else:
            impar += 1
    return par,impar



def main():
    par = 0
    impar = 0

    while True:
        print("Introduce un numero entero positivo")
        num = introducirIntPositivo()
        
        if num ==0:
            break
        
        par,impar = digitosParImpar(num,par,impar)

    print(f"Numeros pares introducidos: {par}\nNumeros impares introducidos: {impar}")



if __name__ == "__main__":
    main()