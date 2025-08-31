from flask import Blueprint, request, jsonify
from utils.decorators import token_required, admin_required, member_required
from extensions import mongo  # עכשיו זה מייבא מ-extensions ולא מ-main
from bson import ObjectId  # ✅ ייבוא נכון של ObjectId

users_bp = Blueprint('users', __name__)

# ✨ פונקציה עזר להמרת ObjectId ל־string
def serialize_user(user_doc):
    return {
        "id": str(user_doc.get("_id", "")),
        "full_name": str(user_doc.get("full_name", "")),
        "email": str(user_doc.get("email", "")),
        "tz": str(user_doc.get("tz", "")),
        "address": str(user_doc.get("address", "")),
        "role": str(user_doc.get("role", ""))
    }


@users_bp.route('/users', methods=['GET'])
@token_required
@member_required
def get_users(current_user):
    try:
        users = list(mongo.db.users.find({}))
        users = [serialize_user(u) for u in users]
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@users_bp.route('/users/<user_id>', methods=['GET'])
@admin_required
def get_user(current_user, user_id):
    try:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user:
            return jsonify(serialize_user(user))
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@users_bp.route('/users/<user_id>', methods=['DELETE'])
@admin_required
def delete_user(current_user, user_id):
    if str(current_user['_id']) == user_id:
        return jsonify({"error": "Cannot delete yourself"}), 400
    try:
        result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            return jsonify({"message": "User not found"}), 404
        return jsonify({"message": "User deleted"})
    except Exception as e:
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

@users_bp.route('/users/<user_id>', methods=['PUT'])
@admin_required
def update_user(current_user, user_id):
    data = request.get_json()
    update_data = {
        "full_name": data.get('full_name'),
        "tz": data.get('tz'),
        "email": data.get('email'),
        "address": data.get('address'),
        "role": data.get('role')
    }
    # הסרת ערכים None
    update_data = {k: v for k, v in update_data.items() if v is not None}

    # עדכון סיסמה אם יש
    if data.get('password'):
        from werkzeug.security import generate_password_hash
        update_data['password'] = generate_password_hash(data['password'])

    try:
        result = mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        if result.matched_count == 0:
            return jsonify({"message": "User not found"}), 404
        return jsonify({"message": "User updated"})
    except Exception as e:
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

@users_bp.route('/users/<user_id>/role', methods=['PUT'])
@admin_required
def update_user_role(current_user, user_id):
    data = request.get_json()
    new_role = data.get('role')

    if new_role not in ['admin', 'member', 'user']:
        return jsonify({"error": "Invalid role"}), 400
    if str(current_user['_id']) == user_id:
        return jsonify({"error": "Cannot change your own role"}), 400

    try:
        result = mongo.db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"role": new_role}}
        )
        if result.matched_count == 0:
            return jsonify({"message": "User not found"}), 404

        updated_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return jsonify({"message": f"User role updated to '{new_role}'", "user": serialize_user(updated_user)})
    except Exception as e:
        return jsonify({'error': 'Database error', 'message': str(e)}), 500
