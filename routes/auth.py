from flask import Blueprint, request, jsonify, make_response,Response
from extensions import db
from models.user import User
import jwt
import datetime
from dotenv import load_dotenv
import os 
import json
from utils.decorators import token_required
load_dotenv()
secret_key = os.getenv('SECRET_KEY')
token_key = os.getenv('TOKEN_KEY')
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/protected')
def protected():
    token = request.cookies.get(token_key)
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401

    try:
        payload = jwt.decode(token, token_key, algorithms=['HS256'])
        user_id = payload['user_id']
        # אפשר להמשיך לעבוד עם user_id
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

        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email already registered'}), 400

        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({"error": "Email already exists"}), 400

        new_user = User(
            full_name=data['full_name'],
            tz=data['tz'],
            email=data['email'],
            address=data['address'],
            role='user',
        )

        new_user.set_password(data['password'])

        db.session.add(new_user)
        db.session.commit()
        json_str = json.dumps(new_user.to_dict(), ensure_ascii=False)

        return Response(json_str, content_type='application/json; charset=utf-8')

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'message': 'Missing email or password'}), 400

        user = User.query.filter_by(email=data['email']).first()
        if not user:
            return jsonify({'message': 'Invalid credentials'}), 401

        if not user.check_password(data['password']):
            return jsonify({'message': 'Invalid credentials'}), 401

        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, token_key, algorithm='HS256')

        response = make_response(jsonify({'message': 'Login successful'}))
        # שמירת ה-token בעוגיה
        response.set_cookie(
            token_key,
            token,
            httponly=True,          # מונע גישה מ-JS בצד לקוח (מומלץ לאבטחה)
            secure=False, # <--- כאן
            samesite='Lax',         # להגבלת שיתוף העוגיה בין אתרים
            max_age=360000,         # זמן חיים של העוגיה בשניות (כאן שעה)
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
           secure=False, # וודא שזה מתאים למה שמוגדר ב-login endpoint
           samesite='Lax',
           path='/' # <--- זה הדבר החשוב שצריך לוודא שקיים ותואם
       )    
    return response

@auth_bp.route('/me', methods=['GET'])
@token_required
def who_am_i(current_user):
    return jsonify(current_user.to_dict())
