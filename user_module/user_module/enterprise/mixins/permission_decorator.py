from functools import wraps
from typing import Callable


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get("data")
        if not token:
            return data, status
        return f(*args, **kwargs)

    return decorated


def admin_token_required(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status

        admin = token.get("admin")
        if not admin:
            response_object = {"status": "fail", "message": "admin token required"}
            return response_object, 401

        return f(*args, **kwargs)

    return decorated


def permission(leval=None):
    def permission_wr(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            data, status = Auth.get_permission_lavel(request)
            token = data.get("data")
            if not token:
                return data, status
            if leval not in token["permissions"]:
                response_object = {"status": "fail", "message": "admin token required"}
                return response_object, 401
            return f(*args, **kwargs)

        return wrap

    return permission_wr
