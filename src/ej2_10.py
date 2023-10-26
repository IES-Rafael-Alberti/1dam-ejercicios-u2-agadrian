'''
Ejercicio 2.1.10

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los -ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

def eleccionPizza():
    '''
    Pregunta si quiere piza vegetariana siendo la unica opcion de respuesta "si" o "no"

    Retorna:
            str --> "vegetariana"
                    "no vegetariana"
    '''

    
    while True:
        eleccion = input("Quieres piza vegetariana? (si/no): \n").lower()
        if eleccion not in ["si", "no"]:
            print("ERROR - Debes responder con (si/no)") 
        else:
            if eleccion == "si":
                return "vegetariana"
            else:
                return "no vegetariana"




def menuPizza(eleccion):
    ingredientes_veg = ["pimiento","tofu"]
    ingredientes_no_veg = ["peperoni","jamón","salmón"]
    if eleccion == "vegetariana":
        print("Elije un solo ingrediente para añadir:", ", ".join(ingredientes_veg))
        opc = input()

        salir = False
        while not salir:
            if opc not in ingredientes_veg:
                print("ERROR - Debes elejir uno de los ingredientes")
                opc = input()
            else:
                salir = True
        return opc
    else:
        print("Elije un solo ingrediente para añadir: " + ", ".join(ingredientes_no_veg))
        opc = input()

        salir = False
        while not salir:
            if opc not in ingredientes_no_veg:
                print("ERROR - Debes elejir uno de los ingredientes")
                opc = input()
            else:
                salir = True
        return opc
        


def main():
    tipoPizza = eleccionPizza()
    ingrediente = menuPizza(tipoPizza)
    
    

    print("Ha elegido una piza " + tipoPizza + ", con los siguientes ingredientes: tomate, mozzarrella, " + ingrediente + ".")

    



if __name__ == "__main__":
    main()