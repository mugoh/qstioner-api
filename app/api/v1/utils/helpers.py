from functools import wraps
from flask import request

from ...v1.models.users import UserModel
from ...v1.views.user import get_jwt_identity


def verify_pass(value):
    if len(value) < 6:
        raise ValueError("Password should be at least 6 charcters")
    return value


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        # We never get here in real sense, consumed by missing Auth header
        # Uncomment when testing manually
        #
        # Verify Logged in
        """if not get_jwt_identity():
            return {
                "Status": 403,
                "Error": "Please log in, okay?"
            }, 403

        user = UserModel.get_by_name(get_jwt_identity())
        if not user:
            return {
                "Status": 400,
                "Error": "Identity unknown"
            }
    """
        if not UserModel.get_by_name(get_jwt_identity()).isAdmin:
            return {
                "Status": 403,
                "Message": "Oops! Only an admin can do that"
            }, 403
        return f(*args, **kwargs)
    return wrapper


def current_user_only(f):
    @wraps(f)
    def wrapper(*args, **kwars):
        url_user_field = request.base_url.split('/')
        user = url_user_field[-2]
        this_user = get_jwt_identity()

        if not this_user:
            return {
                "Status": 403,
                "Message": "You need to be logged in to do that"
            }, 403

        try:
            uid = int(user)
            user = UserModel.get_by_id(uid)
            if user:
                user = user.username
            print(user)
        except ValueError:
            user = user
        if this_user != user:
            return {
                "Status": 403,
                "Error": "Denied. Not accessible to current user"
            }, 403
        return f(*args, **kwars)
    return wrapper
