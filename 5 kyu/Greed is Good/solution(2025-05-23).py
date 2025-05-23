def score(dice: list):
    result = 0
    for i in set(dice):
        combination = dice.count(i)
        if combination >= 3:
            if i == 1:
                result += 1000 + (combination - 3) * 100
            elif i == 5:
                result += 500 + (combination - 3) * 50
            else:
                result += i * 100
        else:
            if i == 1:
                result += combination * 100
            elif i == 5:
                result += combination * 50
    return result