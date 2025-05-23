def validate_pin(pin):
    try:
        pin = list(map(int, pin))
        if len(pin) != 4 and len(pin) != 6:
            raise ValueError
        return True
    except:
        return False