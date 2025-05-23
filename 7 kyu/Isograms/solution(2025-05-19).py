def is_isogram(string):
    string = sorted(string.lower())
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True