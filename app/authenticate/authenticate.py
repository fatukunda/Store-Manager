from functools import wraps
from flask import jsonify, request

def check_auth(username, password):
    return username == 'admin' and password == 'admin'

def authenticate_path():
    message = {'message': "You need admin authorization to access this page"}
    response = jsonify(message)
    response.status_code = 401
    response.headers['Basic Auth'] = 'admin'
    return response

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth: 
            return authenticate_path()

        elif not check_auth(auth.username, auth.password):
            return authenticate_path()
        return f(*args, **kwargs)

    return decorated
