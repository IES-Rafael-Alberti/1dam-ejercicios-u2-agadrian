'''
Ejercicio 2.2.13

Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''

def ecoInput():
    '''
    Pide texto e imprime el texto introducido. Acaba al introducir "salir".
    '''
    texto = input("Introduce lo que quieras. Para salir introduce 'salir': \n")
    while texto != 'salir':
        print(texto)
        texto = input()
    print("Adiós!")
    


def main():
    
    ecoInput()



if __name__ == "__main__":
    main()