from flask import Blueprint, request, jsonify, make_response, Response
from extensions import mongo
import jwt
import datetime
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
from utils.decorators import token_required
import json

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
token_key = os.getenv('TOKEN_KEY')

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# ✨ פונקציה עזר להמרת MongoDB document ל־JSON
def serialize_user(user_doc):
    user_doc['_id'] = str(user_doc['_id'])
    user_doc.pop('password', None)  # הסרת הסיסמה מהתשובה
    return user_doc

@auth_bp.route('/protected')
def protected():
    token = request.cookies.get(token_key)
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401

    try:
        payload = jwt.decode(token, token_key, algorithms=['HS256'])
        user_id = payload['user_id']
        return jsonify({'message': f'Welcome user {user_id}!'})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expired!'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token!'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Missing email or password'}), 400

        existing_user = mongo.db.users.find_one({"email": data['email']})
        if existing_user:
            return jsonify({"error": "Email already exists"}), 400

        new_user = {
            "full_name": data.get('full_name'),
            "tz": data.get('tz'),
            "email": data['email'],
            "address": data.get('address'),
            "role": 'user',
            "password": generate_password_hash(data['password'])
        }

        result = mongo.db.users.insert_one(new_user)
        new_user['_id'] = str(result.inserted_id)
        new_user.pop('password')

        return Response(json.dumps(new_user, ensure_ascii=False), content_type='application/json; charset=utf-8')

    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        if not isinstance(email, str) or not isinstance(password, str):
            return jsonify({"error": "Expected a string value", "message": "Email and password must be strings"}), 500
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Missing email or password'}), 400

        user = mongo.db.users.find_one({"email": data['email']})
        if not user or not check_password_hash(user['password'], data['password']):
            return jsonify({'message': 'Invalid credentials'}), 401

        token = jwt.encode({
            'user_id': str(user['_id']),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, token_key, algorithm='HS256')

        response = make_response(jsonify({'message': 'Login successful'}))
        response.set_cookie(
            token_key,
            token,
            httponly=True,
            secure=False,  # אפשר לשנות ל-True ב-HTTPS
            samesite='Lax',
            max_age=3600,  # 1 שעה
            path='/'
        )
        return response
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({'message': 'Logout successful'}))
    response.set_cookie(
        token_key,
        '',
        expires=0,
        httponly=True,
        secure=False,
        samesite='Lax',
        path='/'
    )
    return response

# auth.py או auth_bp
@auth_bp.route('/me', methods=['GET'])
@token_required
def who_am_i(current_user):
    try:
        # הסרת הסיסמה מהתשובה
        user_data = current_user.copy()
        user_data.pop('password', None)
        user_data['_id'] = str(user_data['_id'])  # המרת ObjectId ל-string
        return jsonify(user_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
