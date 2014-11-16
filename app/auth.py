from flask import request, Response
from functools import wraps
from app import app

def check_auth(username, password):
    """
    Check submitted auth values.
    """
    return username == app.config['AUTH_USER'] and password == app.config['AUTH_PASS']

def authenticate():
    """
    Returns a 401 response if auth is invalid.
    """
    return Response(
            'Nuh-uh-uh, you didn\'t say the magic word!',
            401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    """
    Decorator for routes requiring authentication.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated
