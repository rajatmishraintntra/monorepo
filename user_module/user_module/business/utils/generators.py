import jwt
import os
import bcrypt
import json


def generate_token(payload: dict):
    secret = os.getenv("secret_key")
    return jwt.encode(payload, secret, algorithm="HS256")


def decode_token(token: str):
    secret = os.getenv("secret_key")
    return jwt.decode(token, secret, algorithms=["HS256"])


def generate_password_hash(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def verify_password_hash(password, hashed):
    if bcrypt.checkpw(password, hashed):
        return True
    else:
        return False
