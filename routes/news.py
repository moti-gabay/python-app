# routes/news_bp.py (או הקובץ בו מוגדר ה-Blueprint של החדשות)
from flask import Blueprint, request, jsonify
from extensions import db # וודא ש-db מיובא נכון
from models.news import NewsItem # וודא ש-NewsItem מיובא נכון
from utils.decorators import token_required, admin_required # ייבוא דקורטורים לאימות והרשאה
from utils.util import json_response

news_bp = Blueprint('news', __name__, url_prefix='/news')

# נקודת קצה ליצירת פריט חדשות חדש
@news_bp.route('/', methods=['POST'])
@token_required # דורש שהמשתמש יהיה מחובר
@admin_required # דורש שהמשתמש יהיה אדמין כדי ליצור חדשות
def create_news_item(current_user): # הפונקציה מקבלת את current_user מהדקורטור
    print(f"Admin {current_user.email} is attempting to create a news item.")
    try:
        data = request.get_json() # קבל את גוף הבקשה כ-JSON

        # ולידציה: וודא ששדות חובה קיימים
        if not data:
            print("No JSON data provided in request.")
            return jsonify({'message': 'No input data provided'}), 400
        
        # שינוי: וודא שבודקים את השדות הנכונים: 'title' ו-'full_content'
        if not data.get('title') or not data.get('full_content'):
            missing_fields = []
            if not data.get('title'):
                missing_fields.append('title')
            if not data.get('full_content'):
                missing_fields.append('full_content')
            
            error_message = f"Missing required fields: {', '.join(missing_fields)}"
            print(f"Validation Error: {error_message}. Received data keys: {data.keys()}")
            return jsonify({'message': error_message}), 400

        # יצירת אובייקט NewsItem חדש
        new_news_item = NewsItem(
            title=data['title'],
            description=data.get('description'), # אופציונלי
            full_content=data['full_content'],
            image_url=data.get('image_url') # אופציונלי
            # published_at יוגדר אוטומטית במודל אם לא סופק
        )

        db.session.add(new_news_item)
        db.session.commit()
        print(f"News item '{new_news_item.title}' created successfully by {current_user.email}.")
        return jsonify({'message': 'News item created successfully', 'news_item': new_news_item.to_dict()}), 201

    except Exception as e:
        print(f"Error creating news item: {e}")
        db.session.rollback() # בצע rollback במקרה של שגיאה בבסיס נתונים
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# --- נקודות קצה נוספות לחדשות (GET, PUT, DELETE) יבואו כאן ---
# לדוגמה:
@news_bp.route('/', methods=['GET'])
def get_all_news_items():
    try:
        news_items = NewsItem.query.all()
        return json_response([item.to_dict() for item in news_items]), 200
    except Exception as e:
        print(f"Error fetching news items: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@news_bp.route('/<int:news_id>', methods=['GET'])
def get_news_item(news_id):
    try:
        news_item = NewsItem.query.get(news_id)
        if not news_item:
            return jsonify({'message': 'News item not found'}), 404
        return jsonify(news_item.to_dict()), 200
    except Exception as e:
        print(f"Error fetching news item {news_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@news_bp.route('/<int:news_id>', methods=['PUT', 'PATCH'])
@token_required
@admin_required
def update_news_item(current_user, news_id):
    print(f"Admin {current_user.email} is attempting to update news item ID: {news_id}.")
    try:
        news_item = NewsItem.query.get(news_id)
        if not news_item:
            return jsonify({'message': 'News item not found'}), 404

        data = request.get_json()
        if not data:
            return jsonify({'message': 'No input data provided'}), 400

        news_item.title = data.get('title', news_item.title)
        news_item.description = data.get('description', news_item.description)
        news_item.full_content = data.get('full_content', news_item.full_content)
        news_item.image_url = data.get('image_url', news_item.image_url)
        # ניתן לעדכן גם published_at אם רוצים, אך לרוב הוא נשאר כפי שפורסם לראשונה
        
        db.session.commit()
        print(f"News item {news_id} updated successfully by {current_user.email}.")
        return jsonify({'message': 'News item updated successfully', 'news_item': news_item.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error updating news item {news_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@news_bp.route('/<int:news_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_news_item(current_user, news_id):
    print(f"Admin {current_user.email} is attempting to delete news item ID: {news_id}.")
    try:
        news_item = NewsItem.query.get(news_id)
        if not news_item:
            return jsonify({'message': 'News item not found'}), 404
        
        db.session.delete(news_item)
        db.session.commit()
        print(f"News item {news_id} deleted successfully by {current_user.email}.")
        return jsonify({'message': 'News item deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting news item {news_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500
