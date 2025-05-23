def move_zeros(lst):
    return [i for i in lst if i != 0] + [0 for x in range(lst.count(0))]