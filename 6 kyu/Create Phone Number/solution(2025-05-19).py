def create_phone_number(n):
    s =  ''.join(map(str, n))
    return f'({s[0: 3]}) {s[3: 6]}-{s[6:]}'
