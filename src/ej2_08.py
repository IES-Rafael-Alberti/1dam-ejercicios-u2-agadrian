'''
Ejercicio 2.1.8

En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	        Puntuación
Inaceptable	    0.0
Aceptable	    0.4
Meritorio	    0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''



def nivelRendimiento(puntuacion):
    '''
    Recibe un parametro puntuacion de tipo float. Lo usa para calcular el nivel de rendimiento del empleado

    Retorna:
            str de el valor del nivel de rendimiento o de error del valor del dato introducido
    
    '''
    if puntuacion == 0.0:
        return "Inaceptable"
    elif puntuacion == 0.4:
        return "Aceptable"
    elif puntuacion >= 0.6:   
        return "Meritorio"
    else:
        return "Error"


def main():
    puntuacion = float(input("Puntuación del usuario: \n"))
    rendimiento = nivelRendimiento(puntuacion)
    dinero = puntuacion * 2400
    if rendimiento == "Error":
        print("ERROR - El valor debe ser uno de los establecidos previamente (0.0 , 0.4 , 0.6 o más )")
    else:
        print(f"Tu nivel de rendimiento es: {rendimiento}, y tu dinero correspondiente será {dinero}€")



if __name__ == "__main__":
    main()

