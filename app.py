from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from extensions import db, migrate, mail, cors # <--- וודא ש-mail ו-cors מיובאים כאן
import json
from dotenv import load_dotenv
import os 

load_dotenv() 

def create_app():
    app = Flask(__name__) # אתחול האפליקציה חייב להיות ראשון

    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads') # לדוגמה, תיקייה בשם 'uploads' בתיקיית העבודה הנוכחית
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # וודא שמשתני הסביבה נטענים לפני השימוש בהם
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("DB_DRIVER").replace(" ", "+")  # חייבים להמיר רווחים ל+


    secret_key = os.getenv('SECRET_KEY')
    
    params = (
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    # הגדרות אפליקציה
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # מקסימום גודל להעלאה: 16MB (אפשר לשנות)

    IMAGES_UPLOAD_FOLDER = 'uploaded_images'
    app.config['IMAGES_UPLOAD_FOLDER'] = IMAGES_UPLOAD_FOLDER
    os.makedirs(IMAGES_UPLOAD_FOLDER, exist_ok=True) # וודא שהתיקייה קיימת

    # הגדרות Flask-Mail - חייבות להיות לפני mail.init_app(app)
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() in ['true', '1', 't']
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER') # כתובת האימייל של השולח
    app.config['SITE_OWNER_EMAIL'] = os.getenv('SITE_OWNER_EMAIL') # <--- וודא שזה קיים

    # app.config.from_pyfile('config.py') # <--- שים לב: אם יש לך config.py, וודא שאין סתירות

    # אתחול הרחבות - סדר חשוב!
    db.init_app(app)
    migrate.init_app(app, db) # צריך את האפליקציה ואת ה-db
    cors.init_app(app, resources={r"/*": {
        "origins": "http://localhost:4200", # <--- חייב להתאים בדיוק למקור של אפליקציית Angular
        "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"], # <--- וודא ש-POST ו-OPTIONS כלולים
        "allow_headers": ["Content-Type", "Authorization", "X-Access-Tokens"], # <--- וודא שכל הכותרות הרלוונטיות כלולות
        "supports_credentials": True # <--- חייב להיות True אם אתה שולח קוקיז
    }})    
    mail.init_app(app) # <--- זה חסר! חייב להיות כאן!

    # ייבוא ורישום Blueprint-ים - אחרי אתחול הרחבות
    from routes.auth import auth_bp
    from routes.users import users_bp
    from routes.events import events_bp
    from routes.news import news_bp
    from routes.uploads import uploads_bp
    from routes.image import image_bp
    from routes.email import email_bp # <--- ייבוא ה-Blueprint החדש (ודא שזה email_bp.py)
    from routes.tradition import tradition_bp # <--- ייבוא ה-Blueprint החדש

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(uploads_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(tradition_bp)
    app.register_blueprint(email_bp, url_prefix='/api') # <--- רישום Blueprint חדש

    @app.route("/" ,methods=["GET"])
    def index():
        return "Flask server is running"
    
            
    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context(): # <--- זה עדיין חשוב אם אתה מריץ כך
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)

