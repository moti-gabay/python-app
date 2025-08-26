# routes/uploads_bp.py
import os
from flask import Blueprint, request, jsonify, current_app as app, send_from_directory
from werkzeug.utils import secure_filename
from extensions import mongo
from utils.decorators import token_required, admin_required, member_required
from utils.util import mongo_doc_to_dict
from datetime import datetime
from bson.objectid import ObjectId

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'png', 'jpg', 'jpeg', 'gif','webp'}

uploads_bp = Blueprint('uploads', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------- UPLOAD FILE ----------------
@uploads_bp.route('/upload', methods=['POST'])
@token_required
@member_required
def upload_file(current_user):
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    category = request.form.get('category')
    year_str = request.form.get('year')
    year = int(year_str) if year_str else None

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = app.config.get('UPLOAD_FOLDER')
        if not upload_folder:
            return jsonify({"message": "Server upload folder not configured"}), 500

        filepath = os.path.join(upload_folder, filename)
        print(current_user)
        try:
            file.save(filepath)
            new_doc = {
                "filename": filename,
                "category": category,
                "year": year,
                "uploaded_by": str(current_user["_id"]),
                "created_at": datetime.utcnow()
            }
            result = mongo.db.uploaded_files.insert_one(new_doc)
            new_doc['_id'] = result.inserted_id
            return jsonify({"message": "File uploaded successfully", "id": str(new_doc['_id'])}), 201
        except Exception as e:
            return jsonify({"message": f"Failed to save file: {str(e)}"}), 500

    return jsonify({"message": "File type not allowed"}), 400

# ---------------- GET ALL FILES ----------------
@uploads_bp.route('/files', methods=['GET'])
@token_required
@member_required
def get_all_files(current_user):
    docs = list(mongo.db.uploaded_files.find())
    return jsonify([mongo_doc_to_dict(doc) for doc in docs]), 200

@uploads_bp.route('/files/debug', methods=['GET'])
def debug_files():
    docs = list(mongo.db.uploaded_files.find())
    return jsonify({
        "count": len(docs),
        "docs": [str(doc) for doc in docs]
    }), 200
# ---------------- VIEW FILE ----------------
@uploads_bp.route('/files/<filename>', methods=['GET'])
@token_required
@admin_required
def view_file(current_user, filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# ---------------- DELETE FILE ----------------
@uploads_bp.route('/files/<string:file_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_file(current_user, file_id):
    try:
        doc = mongo.db.uploaded_files.find_one({"_id": ObjectId(file_id)})
        if not doc:
            return jsonify({'message': 'File not found'}), 404

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], doc['filename'])
        if os.path.exists(file_path):
            os.remove(file_path)

        mongo.db.uploaded_files.delete_one({"_id": ObjectId(file_id)})
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

# ---------------- GET FILES BY YEAR ----------------
@uploads_bp.route('/files/by-year/<int:year>', methods=['GET'])
@token_required
@admin_required
def get_files_by_year(current_user, year):
    docs = list(mongo.db.uploaded_files.find({"year": year}))
    if not docs:
        return jsonify({"message": f"No files found for year {year}"}), 404
    return jsonify([mongo_doc_to_dict(doc) for doc in docs]), 200

# ---------------- GET FILES BY CATEGORY ----------------
@uploads_bp.route('/files/by-category/<string:category>', methods=['GET'])
@token_required
@admin_required
def get_files_by_category(current_user, category):
    docs = list(mongo.db.uploaded_files.find({"category": {"$regex": f"^{category}$", "$options": "i"}}))
    if not docs:
        return jsonify({"message": f"No files found for category '{category}'"}), 404
    return jsonify([mongo_doc_to_dict(doc) for doc in docs]), 200

# ---------------- FILTER FILES ----------------
@uploads_bp.route('/files/filter', methods=['GET'])
@token_required
@member_required
def get_files_filtered(current_user):
    query = {}
    year = request.args.get('year', type=int)
    category = request.args.get('category', type=str)
    if year:
        query['year'] = year
    if category:
        query['category'] = {"$regex": f"^{category}$", "$options": "i"}

    docs = list(mongo.db.uploaded_files.find(query))
    if not docs:
        return jsonify({"message": "No files found matching the criteria"}), 404
    return jsonify([mongo_doc_to_dict(doc) for doc in docs]), 200
