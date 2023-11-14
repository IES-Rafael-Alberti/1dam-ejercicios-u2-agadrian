'''
Ejercicio 2.1.6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''
def pedirTexto():
    '''
    Almacena el texto introducido por consola

    Retorna: str
    '''
    texto = input()
    return texto

def grupoCorrespondiente(nombre, sexo):
    '''
    Recibe dos parametros str, nombre y sexo, y a partir de ellos calcula el grupo perteneciente

    Retorna: str-> "A" or "B"
    '''
    if sexo.lower() == "femenino":
        if nombre.lower() < "m":
            return "A"
        else:
            return "B"
        
    elif sexo.lower() == "masculino":
        if nombre.lower() > "n":
            return "A"
        else: 
            return "B"
    else:
        return "Sexo no valido"



def main():
    print("Introduce nombre: ")
    nombre = pedirTexto()

    print("Introduce sexo (Masculino/Femenino): ")
    sexo = pedirTexto()

    grupo = grupoCorrespondiente(nombre,sexo)
    if grupo == "A" or grupo == "B":
        print(f"Te llamas {nombre} y perteneces al grupo {grupo}")
    else:
        print("Introduce un sexo valido (masculino/femenino)")




if __name__ == "__main__":
    main()