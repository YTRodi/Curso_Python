# --------------------------------------------------- MODULOS
import os

# --------------------------------------------------- CONSTANTES
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}
# --------------------------------------------------- FUNCIONES
def cypher(message):
    words = message.split(' ') #Cuando encontremos un espacio generamos una nueva palabra
    cypher_message = []

    for word in words:
        cypher_word = ''

        for letter in word:

            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)

    return ' '.join(cypher_message) # Por cada espacio, junte nuestra texto cifrado


def decipher(message):
    words = message.split(' ')
    decipher_msge = []

    for word in words:
        decipher_word = ''

        for letter in word:

            for key, value in KEYS.items():

                if value == letter:
                    decipher_word += key

        decipher_msge.append(decipher_word)
    
    return  ' '.join(decipher_msge)

def run():
    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---
            Bienvenido a criptografía. ¿Qué deseas hacer?
            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        Opción:'''))

        if command == 'c':
            msg_input = str(input('Escribe tu mensaje a cifrar:'))
            cypher_message = cypher(msg_input)
            print('Mensaje encriptado con éxito!')
            print(cypher_message)
        elif command == 'd':
            msg_input = str(input('Escribe tu mensaje a descifrar:'))
            decypher_message = decipher(msg_input)
            print(decypher_message)
        elif command == 's':
            break
        else:
            print('¡Comando no encontrado!')
            
        input('Toque una tecla para continuar...')
        os.system('clear')
        
# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":
    print('M E N S A J E S  C I F R A D O S')
    run()