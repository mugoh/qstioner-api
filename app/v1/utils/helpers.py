
def verify_pass(value):
    if len(value) < 6:
        raise ValueError("Password should be at least 6 charcters")
    return value
