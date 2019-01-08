"""
    This file contains the model for users data.
"""
from werkzeug.security import generate_password_hash, check_password_hash

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

    @property
    def password(self):
        return '****'

    @password.setter
    def password(self, pswd):
        self._password = generate_password_hash(pswd)

    def check_password(self, pass_value):

        return check_password_hash(self._password, pass_value)

    def save(self):
        users.append(self)

    #
    # Search behaviours

    @classmethod
    def get_by_name(cls, username):
        found_user = [user for user in users
                      if getattr(user, 'username') == username]

        return found_user if found_user else None

    @classmethod
    def get_by_email(cls, given_email):
        user = [user for user in users
                if getattr(user, 'email') == given_email]
        return user if user else None
