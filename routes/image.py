# routes/image_bp.py
import os
from flask import send_from_directory, Blueprint, request, jsonify, current_app as app
from extensions import db
from utils.decorators import token_required, admin_required, member_required # ייבוא הדקורטורים
from werkzeug.utils import secure_filename
from models.image import Image
from datetime import datetime

image_bp = Blueprint('image_management', __name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# 1. קבלת רשימת כל רשומות התמונות (GET all)
@image_bp.route('/images', methods=['GET'])
@token_required
def get_all_images():
    try:
        images = Image.query.all()
        return jsonify([img.to_dict() for img in images]), 200
    except Exception as e:
        print(f"Error fetching all image records: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500
    
@image_bp.route('/images/<filename>',methods=['GET'])
def uploaded_image(filename):
    return send_from_directory(app.config['IMAGES_UPLOAD_FOLDER'], filename)


# 2. קבלת פרטי רשומת תמונה ספציפית לפי ID (GET by ID)
@image_bp.route('/images/<int:image_id>', methods=['GET'])
@token_required
@member_required # גם חברים וגם מנהלים יכולים לצפות בפרטי תמונה
def get_image_by_id(current_user, image_id):
    print(f"User {current_user.email} (Role: {current_user.role}) is requesting image record ID: {image_id}")
    try:
        image = Image.query.get(image_id)
        if not image:
            return jsonify({'message': 'Image record not found'}), 404
        return jsonify(image.to_dict()), 200
    except Exception as e:
        print(f"Error fetching image record ID {image_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

# 3. מחיקת רשומת תמונה (DELETE)
# פעולה זו צריכה למחוק גם את הקובץ הפיזי וגם את הרשומה במסד הנתונים.
# מוגבלת למנהלים בלבד בגלל ההשפעה על הקבצים הפיזיים.
@image_bp.route('/images/<int:image_id>', methods=['DELETE'])
@token_required
@member_required
# @admin_required # רק מנהלים יכולים למחוק רשומות תמונה וקבצים פיזיים
def delete_image_record(current_user, image_id):
    image_record = Image.query.get(image_id)
    if not image_record:
        return jsonify({'message': 'Image record not found'}), 404
    # --- שלב 1: מחיקת הקובץ הפיזי ---
    image_path = os.path.join(app.config['IMAGES_UPLOAD_FOLDER'], image_record.filename)
    try:
        if os.path.exists(image_path):
            os.remove(image_path)
        db.session.delete(image_record)
        db.session.commit()
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting image record ID {image_id}: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@image_bp.route('/images', methods=['POST'])
@token_required
# @admin_required
@member_required # גם חברים וגם מנהלים יכולים להעלות תמונות
def upload_image_file(current_user):
    print(f"User {current_user.email} (Role: {current_user.role}) is attempting to upload an image file.")
    
    # 1. וודא שקיים קובץ בבקשה (שם השדה הוא 'file')
    if 'file' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400
    
    file = request.files['file']
    
    # 2. וודא שנבחר קובץ ושיש לו שם
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    # 3. וודא שסוג הקובץ מותר (תמונה)
    if not allowed_file(file.filename):
        return jsonify({"message": "File type not allowed. Only PNG, JPG, JPEG, GIF, WEBP are allowed."}), 400

    if file:
        filename = secure_filename(file.filename) # אבטחת שם הקובץ
        images_upload_folder = app.config.get('IMAGES_UPLOAD_FOLDER')
        if not images_upload_folder:
            return jsonify({"message": "Server image upload folder not configured"}), 500
        
        filepath = os.path.join(images_upload_folder, filename)
        
        try:
            file.save(filepath) # שמירת הקובץ הפיזי לדיסק
            print(f"Image file '{filename}' uploaded successfully by {current_user.email}.")
            
            # --- שמירת רשומה במודל Image במסד הנתונים ---
            # ה-URL הציבורי של התמונה (נתיב יחסי עבור frontend)
            image_url_path = f"/images/{filename}" 

            new_image_record = Image(
                filename=filename,
                url=image_url_path,
                uploaded_by=current_user.id,
                uploaded_at=datetime.utcnow() # זמן העלאה
            )
            db.session.add(new_image_record)
            db.session.commit()
            print(f"Image record for '{filename}' saved to DB with ID: {new_image_record.id}")

            # החזרת פרטי התמונה כולל ה-ID החדש ו-URL ללקוח
            return jsonify({"message": "Image uploaded successfully", 
                            "filename": filename, 
                            "url": image_url_path, 
                            "id": new_image_record.id
                           }), 201
        except Exception as e:
            db.session.rollback()
            print(f"Error saving image file or record: {e}")
            return jsonify({"message": f"Failed to save image file or record: {str(e)}"}), 500
    
    return jsonify({"message": "Image upload failed (unknown reason)"}), 500