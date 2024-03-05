import jwt
from datetime import datetime, timezone, timedelta
import config


def encode(payload, secret):
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }
    payload.update({
        "iat": datetime.now(tz=timezone.utc),
        "exp": datetime.now(tz=timezone.utc) + timedelta(hours=1)
    })
    print(payload)
    encoded = jwt.encode(payload, secret, algorithm="HS256")
    print(encoded)
    return encoded


def decode(token, secret):
    return jwt.decode(token, secret, algorithms=["HS256"])


def verify(token, secret):
    try:
        decoded = decode(token, secret)
        if decoded.get('sub', False):
            return True
        return False
    except Exception as e:
        return False


if __name__ == "__main__":
    jwt_token = encode({
      "sub": "114882509371467411056",
      "email": "harshveersa@gmail.com",
      "iat": 1709618749,
      "exp": 1709622349
    }, 'daaadbd71e1f8849975ba2317e43ade5')
    decoded = decode(jwt_token, config.app_secret_key)
    print(decoded)
