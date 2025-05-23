def get_sum(a,b):
    return sum([i for i in range(a if a < b else b, (a if a > b else b) + 1)])