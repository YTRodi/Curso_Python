# --------------------------------------------------- INMUTAR STRINGS
s = "Hola"
# s[0] = "l" #ERROR

# DEBEMOS CREAR OTRA VARIABLE
r = "l" + s[1:]
print(r)

# --------------------------------------------------- FUNCIONES RECURSIVAS
def fact(number):
    if number == 0:
        return 1
    
    return number * fact(number - 1)
    

if __name__ == "__main__":
    num = int(input("Escribe un número: "))

    print(fact(num))