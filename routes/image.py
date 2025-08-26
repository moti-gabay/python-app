# routes/image_bp.py
import os
from flask import send_from_directory, Blueprint, request, jsonify, current_app as app
from extensions import mongo
from utils.decorators import token_required, admin_required, member_required
from werkzeug.utils import secure_filename
from models.image import Image
from datetime import datetime
from bson import ObjectId

image_bp = Blueprint('image_management', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@image_bp.route('/images', methods=['GET'])
@token_required
def get_all_images(current_user):
    try:
        docs = mongo.db.images.find()
        images = [Image.from_mongo(doc).to_dict() for doc in docs]
        return jsonify(images), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@image_bp.route('/images/<filename>', methods=['GET'])
def uploaded_image(filename):
    return send_from_directory(app.config['IMAGES_UPLOAD_FOLDER'], filename)

@image_bp.route('/images/<string:image_id>', methods=['GET'])
@token_required
@member_required
def get_image_by_id(current_user, image_id):
    try:
        doc = mongo.db.images.find_one({"_id": ObjectId(image_id)})
        if not doc:
            return jsonify({'message': 'Image record not found'}), 404
        image = Image.from_mongo(doc)
        return jsonify(image.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@image_bp.route('/images/<string:image_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_image_record(current_user, image_id):
    try:
        doc = mongo.db.images.find_one({"_id": ObjectId(image_id)})
        if not doc:
            return jsonify({'message': 'Image record not found'}), 404
        image = Image.from_mongo(doc)

        image_path = os.path.join(app.config['IMAGES_UPLOAD_FOLDER'], image.filename)
        if os.path.exists(image_path):
            os.remove(image_path)

        mongo.db.images.delete_one({"_id": ObjectId(image_id)})
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@image_bp.route('/images', methods=['POST'])
@token_required
@member_required
def upload_image_file(current_user):
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"message": "File type not allowed"}), 400

    filename = secure_filename(file.filename)
    images_upload_folder = app.config.get('IMAGES_UPLOAD_FOLDER')
    if not images_upload_folder:
        return jsonify({"message": "Server image upload folder not configured"}), 500

    filepath = os.path.join(images_upload_folder, filename)
    try:
        file.save(filepath)

        # השתמש במפתח dict במקום attribute
        uploaded_by_id = str(current_user['_id'])

        image_doc = {
            "filename": filename,
            "url": f"/images/{filename}",
            "uploaded_by": uploaded_by_id,
            "uploaded_at": datetime.utcnow()
        }
        result = mongo.db.images.insert_one(image_doc)
        image_doc['_id'] = str(result.inserted_id)

        return jsonify({
            "message": "Image uploaded successfully",
            "filename": filename,
            "url": image_doc['url'],
            "id": image_doc['_id']
        }), 201
    except Exception as e:
        return jsonify({"message": f"Failed to save image: {str(e)}"}), 500
