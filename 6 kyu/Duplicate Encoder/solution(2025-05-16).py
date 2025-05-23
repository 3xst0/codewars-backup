def duplicate_encode(word):
    word = word.lower()
    count_dict = {}
    for symbol in word:
        count_dict[symbol] = count_dict.get(symbol, 0) + 1
    new_word = ''
    for symbol in word:
        if count_dict[symbol] > 1:
            new_word += ')'
        else:
            new_word += '('
            
    return new_word