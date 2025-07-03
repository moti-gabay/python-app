import os
from flask import Blueprint, request, jsonify, current_app as app
from werkzeug.utils import secure_filename
from models.uploaded_file import UploadedFile
from extensions import db
from utils.decorators import token_required ,admin_required ,member_required # במידה ויש לך מערכת התחברות
from flask import send_from_directory

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'png', 'jpg', 'jpeg', 'gif','webp'}  # כל קבצים

uploads_bp = Blueprint('uploads', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@uploads_bp.route('/upload', methods=['POST'])
@token_required
@member_required # <--- ודא שזה member_required ולא admin_required כאן!
def upload_file(current_user): # הפונקציה חייבת לקבל current_user כפרמטר
    print(f"משתמש {current_user.email} (תפקיד: {current_user.role}) מנסה להעלות קובץ.")
    
    if 'file' not in request.files:
        print("No 'file' part in the request")
        return jsonify({"message": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        print("No selected file")
        return jsonify({"message": "No selected file"}), 400

    category = request.form.get('category')
    year_str = request.form.get('year')
    year = int(year_str) if year_str else None
    
    if file:
        filename = secure_filename(file.filename)
        upload_folder = app.config.get('UPLOAD_FOLDER')
        if not upload_folder:
            print("UPLOAD_FOLDER is not configured in app.config")
            return jsonify({"message": "Server upload folder not configured"}), 500
        
        filepath = os.path.join(upload_folder, filename)
        
        try:
            file.save(filepath)
            new_file = UploadedFile(
                filename=filename,
                category=category,
                year=year,
                uploaded_by=current_user.id # שמירת ID של המשתמש המעלה
            )
            db.session.add(new_file)
            db.session.commit()
            print(f"File {filename} uploaded by user {current_user.email} and saved to DB.")
            return jsonify({"message": "File uploaded successfully", "id": new_file.id}), 201
        except Exception as e:
            db.session.rollback()
            print(f"Error saving file: {e}")
            return jsonify({"message": f"Failed to save file: {str(e)}"}), 500
    
    print("File upload failed (unknown reason)")
    return jsonify({"message": "File upload failed"}), 500



@uploads_bp.route('/files', methods=['GET'])
@token_required
@member_required # רק חברים ומנהלים יכולים לצפות
def get_all_files(current_user): # הפונקציה חייבת לקבל current_user כפרמטר
    print(f"משתמש {current_user.email} (תפקיד: {current_user.role}) מבקש קבצים.")
    files = UploadedFile.query.all()
    # אופציונלי: אם תרצה להציג רק קבצים שהועלו על ידי המשתמש עצמו (בנוסף לתפקיד):
    # if current_user.role == 'user':
    #     files = UploadedFile.query.filter_by(uploaded_by=current_user.id).all()
    return jsonify([file.to_dict() for file in files])


@uploads_bp.route('/files/<filename>', methods=['GET'])
@admin_required  # אם נדרש
def view_file(current_user, filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@uploads_bp.route('/files/<int:file_id>', methods=['DELETE'])
# @token_required
@admin_required
def delete_file(current_user, file_id):
    file = UploadedFile.query.get(file_id)
    if not file:
        return jsonify({'message': 'File not found'}), 404

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    try:
        if os.path.exists(file_path):
            os.remove(file_path)

        db.session.delete(file)
        db.session.commit()

        return jsonify({'message': 'File deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'message': str(e)}), 500

@uploads_bp.route('/files/by-year/<int:year>', methods=['GET'])
# @token_required
@admin_required # אם נדרש
def get_files_by_year(year):
    # מסנן את הקבצים לפי שדה 'year' במודל
    files = UploadedFile.query.filter_by(year=year).all()
    if not files:
        # אפשר להחזיר רשימה ריקה או הודעה מתאימה
        return jsonify({"message": f"No files found for year {year}"}), 404
    return jsonify([file.to_dict() for file in files])

# נקודת קצה לקבלת קבצים לפי קטגוריה
@uploads_bp.route('/files/by-category/<string:category>', methods=['GET'])
# @token_required
@admin_required # אם נדרש
def get_files_by_category(category):
    # מסנן את הקבצים לפי שדה 'category' במודל
    # ניתן להשתמש ב-ilike לחיפוש לא תלוי רישיות (case-insensitive), אם רוצים
    files = UploadedFile.query.filter(UploadedFile.category.ilike(category)).all()
    if not files:
        # אפשר להחזיר רשימה ריקה או הודעה מתאימה
        return jsonify({"message": f"No files found for category '{category}'"}), 404
    return jsonify([file.to_dict() for file in files])

# אופציונלי: נקודת קצה לקבלת קבצים לפי שנה וקטגוריה יחד
@uploads_bp.route('/files/filter', methods=['GET'])
# @token_required
@member_required # אם נדרש
def get_files_filtered():
    year = request.args.get('year', type=int)
    category = request.args.get('category', type=str)

    query = UploadedFile.query

    if year:
        query = query.filter_by(year=year)
    if category:
        query = query.filter(UploadedFile.category.ilike(category))

    files = query.all()

    if not files:
        return jsonify({"message": "No files found matching the criteria"}), 404
    return jsonify([file.to_dict() for file in files])

