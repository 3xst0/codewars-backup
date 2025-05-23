def digital_root(number):
    while True:
        num_as_str = str(number)
        if len(str(num_as_str)) != 1:
            number = 0
            for digit in num_as_str:
                number += int(digit)
        else:
            return number