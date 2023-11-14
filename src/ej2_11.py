'''
Ejercicio 2.2.1

Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

def repetirPalabra(palabra):
    '''
    Almacena en una variable la palabra que recibe por paramtero 10 veces separada por espacio

    Retorna: str cadena de caracteres 
    '''
    resultado = ''
    cont = 0

    while cont < 10:
        resultado += palabra + "\n" 
        cont +=1
    return resultado

    

def main():
    
    palabra = input("Introduce una palabra: \n")

    print(repetirPalabra(palabra))
    


if __name__ == "__main__":
    main()