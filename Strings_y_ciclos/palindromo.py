# --------------------------------------------------- FUNCIONES
def palindrome2(word):
    #Una palabra desde el principio (primer ':') hasta el final (segundo ':') y el -1 revierte la palabra.
    reversed_word = word[::-1] # NOTACIÓN DE SLIDES

    if reversed_word == word:
        return True
    
    return False

def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0,letter) #Agrego en índice 0 la letra nueva.

    reversed_word = "".join(reversed_letters) #Palabra al revés

    if word == reversed_word:
        return True
    else:
        return False

# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":
    word = str(input("Ingrese una palabra: "))

    #if palindrome(word):
    if palindrome2(word):
        print("'{}' si es un palíndromo".format(word))
    else:
        print("No es palíndromo")