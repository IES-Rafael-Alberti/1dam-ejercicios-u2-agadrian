'''
Ejercicio 2.2.1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

def pedirPalabra():
    '''
    Pide una palabra por consola y la almacena

    Retorna:
            str 
    '''
    word = input("Introduce una palabra: \n")

    return word



def main():
    cont = 0
    palabra = pedirPalabra()
    
    while cont < 10:
        print(str(cont+1) + " - " + palabra)
        cont +=1
    


if __name__ == "__main__":
    main()