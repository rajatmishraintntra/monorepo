import os

import bcrypt
import jwt


def generate_token(payload: dict):
    secret_key = os.getenv("SECRET_KEY")
    return jwt.encode(payload, secret_key, algorithm="HS256")


def decode_token(token: str):
    secret_key = os.getenv("SECRET_KEY")
    return jwt.decode(token, secret_key, algorithms=["HS256"])


def generate_password_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def verify_password_hash(password, hashed):
    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False
