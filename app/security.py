from jose import jwt
from datetime import datetime, timedelta


SECRET_KEY = "amazon-secret-key"
ALGORITHM = "HS256"


def create_token(username):

    expire = datetime.utcnow() + timedelta(hours=1)

    data = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token



def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        return username


    except:

        return None