from flask import request
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'  # תיקיית שמירת התמונות
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@content_bp.route('/upload-image', methods=['POST'])
@admin_required
def upload_image(current_user):
    if 'image' not in request.files:
        return jsonify({'message': 'No image part in the request'}), 400
    
    file = request.files['image']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        
        # ודא שתיקיית ההעלאה קיימת
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        file.save(save_path)

        # החזר את הנתיב או ה-URL של התמונה להוספה במערכת
        return jsonify({'message': 'Image uploaded', 'filename': filename}), 201

    return jsonify({'message': 'File type not allowed'}), 400
