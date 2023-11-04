'''
Ejercicio 2.2.23

Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
'''


from ej2_06 import pedirTexto

def digitosEnLinea(titulos):
    '''
    Comprueba y almacena la cantidad de digito que hay en el paramtro

    Retorna:
            int del contador de cantidad de digitos
    '''
    cantDigitos = 0

    for i in titulos:
        if i.isdigit():
            cantDigitos += 1

    return cantDigitos


def main():
    lineas = 0
    titulos = ''
    while True:
        print("Introduce titulo libro (* para salir): ")
        tituloLibros = pedirTexto()

        if tituloLibros == "*":
            break

        titulos = titulos + tituloLibros

        if tituloLibros == "/":
            lineas += 1
            digitos = digitosEnLinea(titulos)
            print(f"Linea completa, aparecen {digitos} digitos numericos")
            titulos = ''
        
    if lineas != 0:
        print(f"Lineas: {lineas}")
        


if __name__ == "__main__":
    main()