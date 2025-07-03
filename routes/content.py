# routes/content.py
from flask import Blueprint, request, jsonify,send_from_directory
from models.page_content import PageContent
from extensions import db
from utils.decorators import admin_required ,member_required,token_required
import json

content_bp = Blueprint('content', __name__, url_prefix='/content')

# קבלת תוכן לפי slug (למשל /content/home)
@content_bp.route('/<string:slug>', methods=['GET'])
@admin_required
def get_page(current_user, slug):
    page = PageContent.query.filter_by(slug=slug).first()
    if not page:
        return jsonify({'message': 'Page not found'}), 404
    return jsonify(page.to_dict())

# יצירת תוכן חדש
@content_bp.route('/', methods=['POST'])
@admin_required
def create_page(current_user):
    data = request.get_json()
    if PageContent.query.filter_by(slug=data['slug']).first():
        return jsonify({'message': 'Page with this slug already exists'}), 400
    
    images_list = data.get('images', [])
    images = json.dumps(images_list, ensure_ascii=False) if images_list else None
    
    new_page = PageContent(
        slug=data['slug'],
        title=data['title'],
        body=data['body'],
        images=images
    )
    
    db.session.add(new_page)
    db.session.commit()
    return jsonify(new_page.to_dict()), 201

# עדכון תוכן קיים
@content_bp.route('/<string:slug>', methods=['PUT'])
@admin_required
def update_page(current_user, slug):
    page = PageContent.query.filter_by(slug=slug).first()
    if not page:
        return jsonify({'message': 'Page not found'}), 404
    data = request.get_json()
    page.title = data.get('title', page.title)
    page.body = data.get('body', page.body)
    db.session.commit()
    return jsonify(page.to_dict())

# מחיקת תוכן
@content_bp.route('/<string:slug>', methods=['DELETE'])
@admin_required
def delete_page(current_user, slug):
    page = PageContent.query.filter_by(slug=slug).first()
    if not page:
        return jsonify({'message': 'Page not found'}), 404
    db.session.delete(page)
    db.session.commit()
    return jsonify({'message': 'Page deleted'})

@content_bp.route('/uploads/<filename>')
@admin_required
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@content_bp.route('/<int:page_id>/images', methods=['PUT', 'PATCH'])
@token_required
@member_required # <--- הרשאת Member: חברים ומנהלים יכולים לעדכן תמונות
def update_page_images(current_user, page_id): # <--- הוסף את 'current_user' כאן!
    print(f"User {current_user.email} (Role: {current_user.role}) is attempting to update images for page ID: {page_id}")
    try:
        page = PageContent.query.get(page_id)
        if not page:
            return jsonify({'message': 'Page content not found'}), 404

        data = request.get_json()
        if not data or 'images' not in data:
            return jsonify({'message': 'Missing "images" array in request body'}), 400
        
        if not isinstance(data['images'], list):
            return jsonify({'message': '"images" must be a list'}), 400
        
        if not all(isinstance(img, str) for img in data['images']):
            return jsonify({'message': 'All image entries must be strings (URLs)'}), 400

        page.images = json.dumps(data['images'])
        db.session.commit()
        
        print(f"Images for page ID {page_id} updated successfully by {current_user.email}.")
        return jsonify({'message': 'Page images updated successfully', 'page': page.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error updating images for page ID {page_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

