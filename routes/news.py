# routes/news_bp.py
from flask import Blueprint, request, jsonify
from extensions import mongo  # חיבור ל-PyMongo
from utils.decorators import token_required, admin_required
from utils.util import mongo_doc_to_dict  # פונקציה שממירה מסמך MongoDB ל-dict
from datetime import datetime
from bson.objectid import ObjectId

news_bp = Blueprint('news', __name__, url_prefix='/news')

# ---------------- CREATE ----------------
@news_bp.route('/', methods=['POST'])
@token_required
@admin_required
def create_news_item(current_user):
    data = request.get_json()
    if not data or not data.get('title') or not data.get('full_content'):
        missing = [f for f in ('title', 'full_content') if not data.get(f)]
        return jsonify({'message': f'Missing required fields: {", ".join(missing)}'}), 400

    try:
        new_doc = {
            "title": data['title'],
            "description": data.get('description'),
            "full_content": data['full_content'],
            "image_url": data.get('image_url'),
            "published_at": data.get('published_at') or datetime.utcnow()
        }
        result = mongo.db.news.insert_one(new_doc)
        new_doc['_id'] = result.inserted_id
        return jsonify({'message': 'News item created', 'news_item': mongo_doc_to_dict(new_doc)}), 201
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- READ ALL ----------------
@news_bp.route('/', methods=['GET'])
def get_all_news_items():
    try:
        docs = list(mongo.db.news.find())
        return jsonify([mongo_doc_to_dict(doc) for doc in docs]), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- READ SINGLE ----------------
@news_bp.route('/<string:news_id>', methods=['GET'])
def get_news_item(news_id):
    try:
        doc = mongo.db.news.find_one({"_id": ObjectId(news_id)})
        if not doc:
            return jsonify({'message': 'News item not found'}), 404
        return jsonify(mongo_doc_to_dict(doc)), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- UPDATE ----------------
@news_bp.route('/<string:news_id>', methods=['PUT', 'PATCH'])
@token_required
@admin_required
def update_news_item(current_user, news_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    try:
        result = mongo.db.news.update_one({"_id": ObjectId(news_id)}, {"$set": data})
        if result.matched_count == 0:
            return jsonify({'message': 'News item not found'}), 404
        doc = mongo.db.news.find_one({"_id": ObjectId(news_id)})
        return jsonify({'message': 'News item updated', 'news_item': mongo_doc_to_dict(doc)}), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- DELETE ----------------
@news_bp.route('/<string:news_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_news_item(current_user, news_id):
    try:
        result = mongo.db.news.delete_one({"_id": ObjectId(news_id)})
        if result.deleted_count == 0:
            return jsonify({'message': 'News item not found'}), 404
        return jsonify({'message': 'News item deleted'}), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# ---------------- GET ALL IDs FOR PRERENDERING ----------------
@news_bp.route('/ids', methods=['GET'])
def get_all_news_ids():
    try:
        # Query the database for all documents and project only the _id field
        docs = mongo.db.news.find({}, {"_id": 1})
        # Convert BSON ObjectId to a string for JSON serialization
        ids = [str(doc['_id']) for doc in docs]
        return jsonify(ids), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500