from flask import Blueprint, request, jsonify
from extensions import db
from models.news import News
from utils.decorators import admin_required

news_bp = Blueprint('news', __name__)

@news_bp.route('/news', methods=['GET'])
def get_news():
    news_items = News.query.order_by(News.created_at.desc()).all()
    return jsonify([n.to_dict() for n in news_items])

@news_bp.route('/news', methods=['POST'])
@admin_required
def create_news(current_user):
    data = request.get_json()
    if not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Missing title or content'}), 400

    news_item = News(title=data['title'], content=data['content'])
    db.session.add(news_item)
    db.session.commit()
    return jsonify(news_item.to_dict()), 201

@news_bp.route('/news/<int:news_id>', methods=['PUT'])
@admin_required
def update_news(current_user, news_id):
    news_item = News.query.get(news_id)
    if not news_item:
        return jsonify({'error': 'News item not found'}), 404

    data = request.get_json()
    news_item.title = data.get('title', news_item.title)
    news_item.content = data.get('content', news_item.content)
    db.session.commit()
    return jsonify(news_item.to_dict())

@news_bp.route('/news/<int:news_id>', methods=['DELETE'])
@admin_required
def delete_news(current_user, news_id):
    news_item = News.query.get(news_id)
    if not news_item:
        return jsonify({'error': 'News item not found'}), 404

    db.session.delete(news_item)
    db.session.commit()
    return jsonify({'message': 'News item deleted successfully'})
