def seq_to_one(n):
    if n > 0:
        return [i for i in reversed(range(1, n + 1))]
    else:
        return [i for i in range(n, 2)]