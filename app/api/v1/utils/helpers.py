"""
    This module contains validators for user data passed in request
    arguments.
"""
from flask import request
import re
from functools import wraps

name_pattern = re.compile(r'^[A-Za-z]+$')


def verify_pass(value):
    if len(value) < 6:
        raise ValueError("Password should be at least 6 charcters")
    return value


def verify_name(value, item):
    if ' ' in value:
        raise ValueError(f'{value} has spaces. {item} should not have spaces')

    elif not name_pattern.match(value):
        raise ValueError(f'Oops! {value} has NUMBERS.' +
                         f' {item} should contain letters only')
    return value


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.json:
            return {
                "Status": 400,
                "Message": "That didn't work" +
                " Please provide a valid json header"
            }
        return f(*args, **kwargs)
    return wrapper
