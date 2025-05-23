def find_outlier(integers):
    remainder = [abs(i) % 2 for i in integers]
    if remainder.count(0) > 1:
        for index, digit in enumerate(remainder):
            if digit == 1:
                return integers[index]
    else:
        for index, digit in enumerate(remainder):
            if digit == 0:
                return integers[index]