"""
    This module contains validators for user data passed in request
    arguments.
"""


def verify_pass(value):
    if len(value) < 6:
        raise ValueError("Password should be at least 6 charcters")
    return value


def verify_names(value, item):
    try:
        int(value)
        raise AttributeError(f"{value} is wrong. {item} cannot be a number")

    except ValueError:
        pass
