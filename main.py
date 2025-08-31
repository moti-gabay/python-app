from flask import Flask, send_from_directory
from extensions import mongo, mail, cors
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()  # טען משתני סביבה

def create_app():
    # אתחול Flask עם תיקיית Angular כסטטית
    app = Flask(
        __name__,
        static_folder='dist/my-angular-app/browser',  # שנה לפי שם תיקיית dist שלך
        static_url_path=''
    )

    # רשימת origins מורשים ל-CORS
    allowed_origins = [
        "http://localhost:4200"
    ]
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": allowed_origins}})

    # תיקיות להעלאות
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    IMAGES_UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploaded_images')
    os.makedirs(IMAGES_UPLOAD_FOLDER, exist_ok=True)

    # משתני סביבה
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')
    app.config['MONGO_URI'] = os.getenv("MONGO_URI")
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['IMAGES_UPLOAD_FOLDER'] = IMAGES_UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['JSON_AS_ASCII'] = False

    # הגדרות Flask-Mail
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() in ['true','1','t']
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    # אתחול הרחבות
    mongo.init_app(app)
    mail.init_app(app)

    # רישום Blueprints
    from routes.auth import auth_bp
    from routes.users import users_bp
    from routes.events import events_bp
    from routes.news import news_bp
    from routes.uploads import uploads_bp
    from routes.image import image_bp
    from routes.email import email_bp
    from routes.tradition import tradition_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(uploads_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(tradition_bp)
    app.register_blueprint(email_bp, url_prefix='/api')

    # מסלול בדיקה ל-Mongo
    @app.route("/test-mongo")
    def test_mongo():
        try:
            mongo.db.test.insert_one({"message": "Hello Atlas"})
            return "MongoDB Atlas connected successfully!"
        except Exception as e:
            return str(e)

    # Serve Angular app
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_angular(path):
        if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.csr.html')

    return app

# 🔹 הוספת משתנה app ברמת המודול עבור Gunicorn
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
