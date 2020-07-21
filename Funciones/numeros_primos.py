import this
# --------------------------------------------------- FUNCIONES
def is_prime(number):

    if number < 2:
        return False

    elif number == 2:
        return True

    elif number > 2 and number % 2 == 0:
        return False

    else:
        for i in range(3, number): #A partir de 3 hasta el número
            if number % i == 0:
                return False

    return True
                
def run():
    #pass # placeholder para decirle a Python que está función no tiene nada todavía
    number  = int(input("Escribe un número: "))
    result = is_prime(number)

    if result is True:
        print("Tú número es primo")
    else:
        print("Tú número no es primo")
    

# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":
    run()
