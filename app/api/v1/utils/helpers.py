"""
    This module contains validators for user data passed in request
    arguments.
"""
import re

name_pattern = re.compile([r'A-Za-z+$'])


def verify_pass(value):
    if len(value) < 6:
        raise ValueError("Password should be at least 6 charcters")
    return value


def verify_name(value, item):
    if ' ' in value:
        raise ValueError(f'{value} has spaces. {item} should not have spaces')

    elif not name_pattern.match(value):
        raise ValueError(f'{value} has NUMBERS. \
            {item} should contain letters only')
    return value
