from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

# JWT
SECRET_KEY = "757222f237e01715d4c004e51930a4457c4f486b6b7b3fe01bef883f7c88c804"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

# Password hashing
# create a new configuration context for password hashing

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# get hash from password
def get_password_hash(password):
    return pwd_context.hash(password)


# verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(encoded_jwt, "encoded")
    return encoded_jwt


def decode_token(token):
    if not token:
        return None
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
