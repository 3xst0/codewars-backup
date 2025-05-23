def rgb(*codes):
        return ''.join([str(match_number_to_letter(clamp(code) // 16)) + str(match_number_to_letter(clamp(code) % 16)) 
                    for code in codes])

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

def clamp(number):
    return max(0, min(255, number))