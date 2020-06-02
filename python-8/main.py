import jwt


def create_token(data, secret):
    encoded = jwt.encode(data, secret, algorithm='HS256')
    return encoded


def verify_signature(token):
    raise NotImplementedError()
