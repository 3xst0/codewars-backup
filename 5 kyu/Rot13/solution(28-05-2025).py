from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase, ascii_letters as letters

def rot13(message: str):
    encrypted_message = ''
    for letter in message:
        if letter not in letters:
            encrypted_message += letter
        elif letter.isupper():
            encrypted_message += uppercase[(uppercase.index(letter) + 13) % len(uppercase)]
        else:
            encrypted_message += lowercase[(lowercase.index(letter) + 13) % len(lowercase)]

    return encrypted_message