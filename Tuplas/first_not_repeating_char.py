# --------------------------------------------------- FUNCIONES
def first_not_repeating_char(char_secuence):
    seen_letter = {}

    for i, letter in enumerate(seen_letter):
        #Verificamos si la letra ya la vimos.
        if letter not in seen_letter:
            # Guardamos el índice y las veces que la vimos (en este caso 1)
            seen_letter[letter] = (i, 1) # Clave: letter - Valor: índice y las veces que vimos esa letra. 
        else:
            seen_letter[letter] = (seen_letter[letter][0], seen_letter[letter][1] + 1)

    '''
    Ejemplo de como quedaria el diccionario:
    'a' : (índice de la 1ra vez que la vimos, cuántas vimos esa letra)
    'b' : (1, 2)
    '''

    final_letters = [] # Va a almacenar una tupla que letras vimos solamente 1 vez y en que índice está
    for key,value in seen_letter.items():
        if value[1] == 1: # Si cada letra la vimos usa sola vez
             final_letters.append( (key,value[0]) )

    # Variable que va a guardar la misma lista pero ORDENADA. 
    # Lambda = función de una línea
    not_repeated_letter = sorted(final_letters, key = lambda value:value[1])

    if not_repeated_letter: # Si tiene algo...
        return not_repeated_letter[0][0] # Regresamos el primer valor
    else:
        return '_'


def sort_order(value):
    '''
    Idem que usar 'lambda'
    '''
    return value[1]    

# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":
    char_secuence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_secuence)

    if result == '_':
        print('Todos los carácteres se repiten')
    else:
        print('El primer caracter no repetido es: {}'.format(result))