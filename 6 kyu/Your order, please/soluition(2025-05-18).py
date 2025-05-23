def order(sentence):
    lst = sentence.split(' ')
    sequence = {}
    for index, word in enumerate(lst):
        for char in word:
            try:
                word_num = int(char)
                sequence[word_num] = index
            except:
                pass
    sorted_dir = sorted(sequence.items())
    new_sentence = ''
    for word_num, index in sorted_dir:
        new_sentence += lst[index] + ' '
    return new_sentence.strip()