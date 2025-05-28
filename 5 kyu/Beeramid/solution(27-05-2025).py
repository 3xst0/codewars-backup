def beeramid(bonus, price):
    available_to_buy = bonus // price
    bought = 0
    levels = 0
    while bought + (levels + 1) ** 2 <= available_to_buy:
        bought += (levels + 1) ** 2
        levels += 1
    return levels