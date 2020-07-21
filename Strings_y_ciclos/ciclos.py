# --------------------------------------------------- FOR LOOP
nombre = "Yago"

# for letter in nombre:
#     print(letter)
#     pass
print("Cantidad de carácteres de la palabra '{}': {}".format(nombre,len(nombre)))

for i in range(30):
    if i % 3 != 0:
        continue
    else:
        print(i**2)

# --------------------------------------------------- WHILE LOOP
import random

def run():
    number_found = False
    rnd_number = random.randint(0,20)
    count = 0

    while not number_found:
        number = int(input("Ingrese un número: "))

        if number == rnd_number:
            print("Felicidades! Encontraste el número en {} intentos!".format(count))
            break
        elif number > rnd_number:
            print("El número es más pequeño")
        else:
            print("El número es más grande")
        
        count += 1
    pass

if __name__ == "__main__":
    run()