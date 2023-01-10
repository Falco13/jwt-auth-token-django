from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime


def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'iat': datetime.datetime.utcnow()
    }, 'access_token_secret', algorithm='HS256')


def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_token_secret', algorithms=['HS256'])
        return payload['user_id']
    except:
        raise AuthenticationFailed('Unauthenticated')


def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_token_secret', algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_token_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise AuthenticationFailed('Unauthenticated')
