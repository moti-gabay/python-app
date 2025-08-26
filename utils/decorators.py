from functools import wraps
from flask import request, jsonify
import jwt
from extensions import mongo
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
token_key = os.getenv('TOKEN_KEY')  # המפתח בו נוצר הטוקן

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get(token_key)
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            payload = jwt.decode(token, token_key, algorithms=['HS256'])
            user_id = payload['user_id']

            # חיפוש המשתמש ב-MongoDB
            current_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
            if not current_user:
                return jsonify({'message': 'User not found!'}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
        except Exception as e:
            return jsonify({'message': 'Error processing token', 'error': str(e)}), 500

        # העברת המשתמש לפונקציה המקושטת
        return f(current_user, *args, **kwargs)

    return decorated

def admin_required(f):
    @wraps(f)
    def decorated_function(current_user, *args, **kwargs):
        # MongoDB document משתמש במילון, לכן משתמשים ב-current_user['role']
        if not current_user or current_user.get('role') != 'admin':
            user_role = current_user.get('role') if current_user else 'None'
            return jsonify({'message': 'Unauthorized – admin only', "role": user_role}), 403

        return f(current_user, *args, **kwargs)
    return decorated_function


def member_required(f):
    @wraps(f)
    def decorated_function(current_user, *args, **kwargs):
        if not current_user:
            return jsonify({'message': 'Authentication required for role check.'}), 401

        # תפקיד 'member' כולל גם תפקיד 'admin' (היררכיה)
        if current_user.get('role') not in ['member', 'admin']:
            print(f"גישה אסורה: משתמש {current_user.get('email')} (תפקיד: {current_user.get('role')}) אינו חבר או מנהל.")
            return jsonify({'message': 'Forbidden: Member access required.', 'role': current_user.get('role')}), 403

        return f(current_user, *args, **kwargs)
    return decorated_function
