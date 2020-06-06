import jwt


def create_token(data, secret):
    encoded = jwt.encode(data, secret, algorithm='HS256')

    if verify_signature(encoded):
        return encoded
    else:
        return False


def verify_signature(token):
    try:
        return jwt.decode(token, 'acelera', algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        return {"error": 2}
