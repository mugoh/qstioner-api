"""
    This module contains the class that creates blacklisted token objects
    and checks for token validity
"""


class Token:

    def __init__(self, token):
        self.signature = token
        self.save(token)

    def save(self):
        blacklisted_tokens.append(self)

    @classmethod
    def check_if_blacklisted(cls, token):
        return any([token for token in blacklisted_tokens if
                    getattr(token, 'signature') == token])


blacklisted_tokens = set()
