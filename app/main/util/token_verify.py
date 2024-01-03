import jwt
import os
from dotenv import load_dotenv
from flask import request, jsonify
from functools import wraps

load_dotenv()

secretKey = os.getenv("SECRET_KEY")

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'X-API-KEY' in request.headers:
            token = request.headers.get('X-API-KEY')
        if not token:
            return {'message': 'Token is missing !!'}, 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, secretKey, algorithms=["HS256"])
            
            return f(decoded_token=data,*args, **kwargs)

        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired !!'}, 401
        except Exception as e:
            print(f"Error: {str(e)}")
            return {'message': 'Token is invalid !!'}, 401

    return decorated
