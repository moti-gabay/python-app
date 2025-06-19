from functools import wraps
from flask import request, jsonify
import jwt
from models.user import User
from extensions import db
from dotenv import load_dotenv
import os 
import json

load_dotenv()
secret_key = os.getenv('SECRET_KEY')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, secret_key, algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
            if not current_user:
                return jsonify({'message': 'User not found!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'message': 'Missing token'}), 401
        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
            user = User.query.get(data['user_id'])
            if not user or user.role != 'admin':
                return jsonify({'message': 'Unauthorized – admin only'," role " : user.role}), 403
            return f(user, *args, **kwargs)
        except Exception as e:
            return jsonify({'message': 'Invalid token', 'error': str(e)}), 401
    return decorated_function


