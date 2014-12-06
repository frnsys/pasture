from flask import request, Response

def authenticate(auth_user, auth_pass):
    """
    Returns a 401 response if auth is invalid.
    """
    auth = request.authorization
    if not auth or not (auth.username == auth_user and auth.password == auth_pass):
        return Response(
                'Nuh-uh-uh, you didn\'t say the magic word!',
                401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
        )
