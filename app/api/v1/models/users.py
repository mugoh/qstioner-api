"""
    This file contains the model for users data.
"""
from werkzeug.security import generate_password_hash, check_password_hash

from .abstract_model import AbstractModel

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

        return found_user[0] if found_user else None

    @classmethod
    def get_by_email(cls, given_email):
        user = [user for user in users
                if getattr(user, 'email') == given_email]
        return user[0] if user else None

    @classmethod
    def get_by_id(cls, usr_id):
        usr = [user for user in users
               if getattr(user, 'id') == usr_id]

        return usr[0] if usr else None

    @classmethod
    def get_all_users(cls):
        return [user.dictify() for user in users]

    def dictify(self):

        return {
            "Firstname": self.firstname,
            "Lastname": self.lastname,
            "Othername": self.othername,
            "Email": self.email,
            "Phonenumber": self.phonenumber,
            "Username": self.username,
            "isAdmin": self.isAdmin,
            "password": self.password,
            "registered": self.created_at,
            "id": self.id
        }

      # return self.__dict__

    def __repr__(self):
        return '{Email} {Username}'.format(**self.dictify())
