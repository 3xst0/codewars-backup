#from preloaded import MORSE_CODE
MORSE_CODE = {}
def decode_morse(morse_code):
    words_list = [word.split(' ') for word in morse_code.strip().split('   ')]
    decoded_word = ''
    for word in  words_list:
        for symbol in word:
            decoded_word += MORSE_CODE.get(symbol)
        decoded_word += ' '
    return decoded_word.strip()