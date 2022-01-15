from flask import request, abort
import os
from get_docker_secret import get_docker_secret

BEARER_KEY = get_docker_secret(os.environ['BEARER_TOKEN_FILE'])


def throw_unauthorized(f):
    '''
    Decorator that calls flask-abort with status code 401 in case of any error
    '''

    def inner(*args, **kws):
        try:
            return f(*args, **kws)
        except:
            abort(401)

    return inner


def authorize(f):
    '''
    Authorization layer
    It checks for a specific Bearer token key in the Authorization layer of the received request
    '''

    @throw_unauthorized
    def inner(*args, **kws):
        data = request.headers['Authorization']
        token = data.split('Bearer ')[1]

        if token != BEARER_KEY:
            abort(401)

        return f(*args, **kws)

    return inner
