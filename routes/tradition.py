# routes/tradition_bp.py
from flask import Blueprint, request, jsonify
from extensions import mongo  # PyMongo
from utils.decorators import token_required, admin_required
from utils.util import mongo_doc_to_dict  # ממיר מסמך MongoDB ל-dict
from datetime import datetime
from bson.objectid import ObjectId

tradition_bp = Blueprint('tradition', __name__)

# ---------------- GET ALL ----------------
@tradition_bp.route('/tradition', methods=['GET'])
def get_all_tradition_items():
    try:
        docs = list(mongo.db.tradition.find())
        return jsonify([mongo_doc_to_dict(doc) for doc in docs]), 200
    except Exception as e:
        print(f"שגיאה בשליפת פריטי מסורת: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- GET SINGLE ----------------
@tradition_bp.route('/tradition/<string:item_id>', methods=['GET'])
def get_tradition_item(item_id):
    try:
        doc = mongo.db.tradition.find_one({"_id": ObjectId(item_id)})
        if not doc:
            return jsonify({'message': 'Tradition item not found'}), 404
        return jsonify(mongo_doc_to_dict(doc)), 200
    except Exception as e:
        print(f"שגיאה בשליפת פריט מסורת {item_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- CREATE ----------------
@tradition_bp.route('/tradition', methods=['POST'])
@token_required
@admin_required
def create_tradition_item(current_user):
    data = request.get_json()
    if not data or not data.get('title') or not data.get('full_content'):
        missing = [f for f in ('title', 'full_content') if not data.get(f)]
        return jsonify({'message': f'Missing required fields: {", ".join(missing)}'}), 400

    try:
        new_doc = {
            "title": data['title'],
            "short_description": data.get('short_description'),
            "full_content": data['full_content'],
            "category": data.get('category'),
            "image_url": data.get('image_url'),
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        result = mongo.db.tradition.insert_one(new_doc)
        new_doc['_id'] = result.inserted_id
        return jsonify({'message': 'Tradition item created', 'item': mongo_doc_to_dict(new_doc)}), 201
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- UPDATE ----------------
@tradition_bp.route('/tradition/<string:item_id>', methods=['PUT', 'PATCH'])
@token_required
@admin_required
def update_tradition_item(current_user, item_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    try:
        data['updated_at'] = datetime.utcnow()
        result = mongo.db.tradition.update_one({"_id": ObjectId(item_id)}, {"$set": data})
        if result.matched_count == 0:
            return jsonify({'message': 'Tradition item not found'}), 404
        doc = mongo.db.tradition.find_one({"_id": ObjectId(item_id)})
        return jsonify({'message': 'Tradition item updated', 'item': mongo_doc_to_dict(doc)}), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- DELETE ----------------
@tradition_bp.route('/tradition/<string:item_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_tradition_item(current_user, item_id):
    try:
        result = mongo.db.tradition.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count == 0:
            return jsonify({'message': 'Tradition item not found'}), 404
        return jsonify({'message': 'Tradition item deleted'}), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500
