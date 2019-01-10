from functools import wraps

from app.v1.models.users import UserModel
from app.v1.views.user import get_jwt_identity


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
