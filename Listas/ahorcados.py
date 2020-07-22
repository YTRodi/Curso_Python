# --------------------------------------------------- MODULOS
import random
import os

# --------------------------------------------------- CONSTANTES
IMG = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''',r'''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''',r'''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''',r'''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''',r'''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''',r'''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''',r'''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''',r'''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''','''
    
    '''
]

WORDS = [
    'secadora',
    'heladera',
    'anteojos',
    'computadora',
    'teclado',
    'mouse',
    'auriculares'
]

TITLE = r''' 
 |  _ \(_)                         (_)   | |                 | |
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___  ___    __ _| |
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \/ __|  / _` | |
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) \__ \ | (_| | |
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/|___/  \__,_|_|
         | |                           | |     | | | |          
     __ _| |__   ___  _ __ ___ __ _  __| | ___ | | | |          
    / _` | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \| | | |          
   | (_| | | | | (_) | | | (_| (_| | (_| | (_) |_|_|_|          
    \__,_|_| |_|\___/|_|  \___\__,_|\__,_|\___/(_|_|_)          
    '''

# --------------------------------------------------- FUNCIONES
def display_board(hidden_word, tries):
    print(IMG[tries])
    print('')
    print(hidden_word)
    print('<-------------------------------------------->')

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def run():
    word = random_word()
    hidden_word = ['-'] * len(word) # Palabra escondida
    tries = 0
    letras_usadas = []

    while True:
        print(TITLE)
        display_board(hidden_word, tries)
        print('Letras usadas: {}\n'.format(letras_usadas))
        current_letter = str(input('Elije una letra: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                print('\nHas perdido! la palabra correcta era {}'.format(word))
                break

        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter
                
                letter_indexes = []
        
        try:
            hidden_word.index('-') # Con la func .index sabemos si quedá alguna barra
        except ValueError:
            print('\nFelicidades! Has ganado! La palabra es: {}'.format(word))
            break


        letras_usadas.append(current_letter)
        os.system('clear')
        
# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":
    run()