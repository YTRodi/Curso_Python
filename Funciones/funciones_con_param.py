# --------------------------------------------------- REGLAS
# Las variables y funciones deben tener nombres distintos
# hello = 'Hola'
# print(hello)

# def helloo():
#     return print("Curso Python")

# saludo = helloo() # Puedo asignar una función a una variable.

# --------------------------------------------------- FUNCIONES
def foreign_exchange_calculator(ammount):
    dollar_to_arg_rate = 71.6051 #tipo de cambio
    
    return dollar_to_arg_rate * ammount

def run():
    print("C A L C U L A D O R A  D E  D I V I S A S")
    print("Convierte dolares a pesos argentinos.")
    print("")

    #cantidad
    ammount = float(input("Ingresa la cantidad de dólares que querés convertir: "))

    result = foreign_exchange_calculator(ammount)

    print("{} dólares son ${} pesos argentinos.".format(ammount,result))
    print("")

# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":
    run()