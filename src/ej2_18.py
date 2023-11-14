
'''
Ejercicio 2.2.8

Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

from ej2_03 import introducirNum

def trianguloRectangulo(num):
    '''
    Crea el triagulo rectangulo y lo almacena en una variable

    Retorna:    
            Str: de la variable triangulo
    '''
    triangulo = ''

    for i in range(1, num*2, 2): #num*2 para que la altura del triangulo sea la introducida como parametro num
        for j in range(i, 0, -2):
            triangulo += str(j) + " "
        triangulo+= "\n"
       
    return triangulo



def main():
    print("Introduce altura del triangulo: ")
    numero = introducirNum()

    print(trianguloRectangulo(numero))



if __name__ == "__main__":
    main()