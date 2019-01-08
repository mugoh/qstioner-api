"""
    This file contains the model for users data.
"""

from abstract_model import AbstractModel

users = []  # Persists user objects


class UserModel(AbstractModel):

    def __init__(self, **kwargs):

        super().__init__(users)
        self.firstname = kwargs['firstname']
        self.lastname = kwargs['lastname']
        self.othername = kwargs['othername']
        self.email = kwargs['email']
        self.phonenumber = kwargs['phonenumber']
        self.username = kwargs['username']
        self.isAdmin = kwargs.get('isAdmin', False)

        self.password = kwargs['password']
