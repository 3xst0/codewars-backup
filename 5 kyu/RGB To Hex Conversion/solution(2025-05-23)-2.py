def rgb(*codes):
    code_in_heximal = ''
    for code in codes:
        code = clamp(code)
        code_in_heximal += str(match_number_to_letter(code // 16)) + str(match_number_to_letter(code % 16))

    return code_in_heximal

def clamp(number):
    return max(0, min(255, number))

def match_number_to_letter(integer):
    match_dict = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    return match_dict.get(integer, integer)