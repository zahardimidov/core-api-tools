import os
import uuid
from datetime import datetime, timedelta, timezone

import jwt
from argon2 import PasswordHasher

SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'my_secret_key')
ALGORITHM = "HS256"

def generate_uuid():
    return str(uuid.uuid4())

def create_jwt_token(data: dict, expire = timedelta(hours=12)) -> str:
    expiration = datetime.now(timezone.utc)
    data.update({"exp": expiration})
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_jwt_token(token: str) -> dict:
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.PyJWTError as e:
        print(e)

pwd_context = PasswordHasher()

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str | bytes, hash: str | bytes):
    return pwd_context.verify(hash, password)