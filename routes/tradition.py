# routes/tradition_bp.py
from flask import Blueprint, request, jsonify
from extensions import db
from models.tradition import TraditionItem # ייבוא המודל החדש
from utils.decorators import token_required, admin_required # ייבוא דקורטורים לאימות והרשאה
from utils.util import json_response
tradition_bp = Blueprint('tradition', __name__, url_prefix='/tradition')

@tradition_bp.route('/', methods=['GET'])
# @token_required # ניתן להגן אם רק משתמשים מחוברים יכולים לראות את התוכן
def get_all_tradition_items():
    """
    מחזיר את כל פריטי המסורת היהודית.
    """
    try:
        items = TraditionItem.query.all()
        return json_response([item.to_dict() for item in items]), 200
    except Exception as e:
        print(f"שגיאה בשליפת פריטי מסורת: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@tradition_bp.route('/<int:item_id>', methods=['GET'])
# @token_required # ניתן להגן אם רק משתמשים מחוברים יכולים לראות את התוכן
def get_tradition_item(item_id):
    """
    מחזיר פריט מסורת בודד לפי ID.
    """
    try:
        item = TraditionItem.query.get(item_id)
        if not item:
            return jsonify({'message': 'Tradition item not found'}), 404
        return jsonify(item.to_dict()), 200
    except Exception as e:
        print(f"שגיאה בשליפת פריט מסורת {item_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@tradition_bp.route('/', methods=['POST'])
@token_required
@admin_required
def create_tradition_item(current_user):
    """
    יוצר פריט מסורת חדש (דורש הרשאת אדמין).
    """
    print(f"Admin {current_user.email} is attempting to create a tradition item.")
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided'}), 400
        
        if not data.get('title') or not data.get('full_content'):
            return jsonify({'message': 'Missing required fields: title or full_content'}), 400

        new_item = TraditionItem(
            title=data['title'],
            short_description=data.get('short_description'),
            full_content=data['full_content'],
            category=data.get('category'),
            image_url=data.get('image_url')
        )
        db.session.add(new_item)
        db.session.commit()
        print(f"Tradition item '{new_item.title}' created successfully by {current_user.email}.")
        return jsonify({'message': 'Tradition item created successfully', 'item': new_item.to_dict()}), 201

    except Exception as e:
        db.session.rollback()
        print(f"שגיאה ביצירת פריט מסורת: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@tradition_bp.route('/<int:item_id>', methods=['PUT'])
@token_required
@admin_required
def update_tradition_item(current_user,item_id):
    """
    מעדכן פריט מסורת קיים (דורש הרשאת אדמין).
    """
    print(f"Admin {current_user.email} is attempting to update tradition item ID: {item_id}.")
    try:
        item = TraditionItem.query.get(item_id)
        if not item:
            return jsonify({'message': 'Tradition item not found'}), 404

        data = request.get_json()
        print(data)
        if not data:
            return jsonify({'message': 'No input data provided'}), 400

        item.title = data.get('title', item.title)
        item.short_description = data.get('short_description', item.short_description)
        item.full_content = data.get('full_content', item.full_content)
        item.category = data.get('category', item.category)
        item.image_url = data.get('image_url', item.image_url)
        
        db.session.commit()
        print(f"Tradition item {item_id} updated successfully by {current_user.email}.")
        return jsonify({'message': 'Tradition item updated successfully', 'item': item.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        print(f"שגיאה בעדכון פריט מסורת {item_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@tradition_bp.route('/<int:item_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_tradition_item(current_user, item_id):
    """
    מוחק פריט מסורת (דורש הרשאת אדמין).
    """
    print(f"Admin {current_user.email} is attempting to delete tradition item ID: {item_id}.")
    try:
        item = TraditionItem.query.get(item_id)
        if not item:
            return jsonify({'message': 'Tradition item not found'}), 404
        
        db.session.delete(item)
        db.session.commit()
        print(f"Tradition item {item_id} deleted successfully by {current_user.email}.")
        return jsonify({'message': 'Tradition item deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"שגיאה במחיקת פריט מסורת {item_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500
