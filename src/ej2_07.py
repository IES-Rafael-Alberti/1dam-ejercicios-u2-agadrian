'''
Ejercicio 2.1.7

Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''



def tipoImpositivo(rentaAnual):
    '''
    Recibe un parametro tipo float, y calcula el tipo de impositivo 
    que le corresponde a dicho parametro

    Retorna: 
            int 
    '''
    if rentaAnual < 10000:
        return 5
    elif rentaAnual >= 10000 and rentaAnual < 20000:
        return 15
    elif rentaAnual >= 20000 and rentaAnual < 35000:
        return 20
    elif rentaAnual >= 35000 and rentaAnual < 60000:
        return 30
    else:
        return 45
    


def main():
    renta = float(input("Introduce tu renta anual: \n"))
    if renta < 0:
        print("ERROR - La renta debe ser un valor positivo.")
    else:
        impositivo = tipoImpositivo(renta)
        print(f"Para una renta de {renta}€ anuales, el tipo impositivo es del {impositivo}%")




if __name__ == "__main__":
    main()