from flask import Blueprint, request, jsonify ,Response
from extensions import db
from models.user import User
from utils.decorators import token_required ,admin_required
import json

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'])
@admin_required
def get_users(current_user):
    try:
        users = User.query.all()
        users_list = [user.to_dict() for user in users]
        
        json_str = json.dumps(users_list, ensure_ascii=False)
        
        return Response(json_str, content_type='application/json; charset=utf-8')
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@users_bp.route('/<int:user_id>', methods=['GET'])
@admin_required
def get_user(current_user, user_id):
    try:

        user = User.query.get(user_id)
        if user:
            return jsonify(user.to_dict())
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@users_bp.route('/<int:user_id>', methods=['DELETE'])
@admin_required
def delete_user(current_user, user_id):
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    
    if current_user.id == user_id:
        return jsonify({"error": "Cannot delete yourself"}), 400
    
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

    return jsonify({"message": "User deleted"})

@users_bp.route('/<int:user_id>', methods=['PUT'])
@admin_required
def update_user(current_user, user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    user.full_name = data.get('full_name', user.full_name)
    user.tz = data.get('tz', user.tz)
    user.email = data.get('email', user.email)
    user.address = data.get('address', user.address)
    user.role = data.get('role', user.role)

    if 'password' in data and data['password']:
        user.set_password(data['password'])

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

    return jsonify({"message": "User updated"})

@users_bp.route('/<int:user_id>/role', methods=['PUT'])
@admin_required
def update_user_role(current_user, user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    if user.id == current_user.id:
        return jsonify({"error": "Cannot change your own role"}), 400

    data = request.get_json()
    new_role = data.get('role')

    if new_role not in ['admin', 'member', 'user']:
        return jsonify({"error": "Invalid role"}), 400

    try:
        user.role = new_role
        db.session.commit()
        return jsonify({"message": f"User role updated to '{new_role}'", "user": user.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500
