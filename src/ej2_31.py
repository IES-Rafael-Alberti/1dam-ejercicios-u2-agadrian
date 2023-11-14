'''
Ejercicio 2.2.21

Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
'''

from ej2_03 import introducirNum


def totalAPagar(ventas):
    '''
    Se le pasa como parametro la cantidad del valor de las venta y le resta el 10% si es necesario

    Retorna: int del total tras comprobar si posee descuento
    '''
    if ventas > 1000:
        ventas = ventas - (ventas*0.10)
    return ventas


def main():
    ventas = 0

    while True:
        print("Introduce monto de la compra(0 para salir): ")
        monto = introducirNum()

        if monto == 0:
            break

        ventas += monto

    if ventas != 0:
        total = totalAPagar(ventas)
        print(f"El total a pagar sera de {total}")
        
    print("Saliendo...")



if __name__ == "__main__":
    main()