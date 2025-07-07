from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from extensions import db, migrate, mail, cors # <--- וודא ש-mail ו-cors מיובאים כאן
import json
from dotenv import load_dotenv
import os 
# from flask_cors import CORS # <--- אין צורך לייבא כאן אם הוא ב-extensions.py
# from routes.email import email_bp # <--- אין צורך לייבא כאן, נייבא בתוך create_app()

load_dotenv() 

def create_app():
    app = Flask(__name__) # אתחול האפליקציה חייב להיות ראשון

    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads') # לדוגמה, תיקייה בשם 'uploads' בתיקיית העבודה הנוכחית
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # וודא שמשתני הסביבה נטענים לפני השימוש בהם
    server = os.getenv('SQL_SERVER')
    database = os.getenv('SQL_DATABASE')
    trusted_conn = os.getenv('SQL_TRUSTED_CONNECTION')
    secret_key = os.getenv('SECRET_KEY')
    
    params = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection={trusted_conn};"
        f"UnicodeResults=True;"
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
    cors.init_app(app, resources={r"/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)
    mail.init_app(app) # <--- זה חסר! חייב להיות כאן!

    # ייבוא ורישום Blueprint-ים - אחרי אתחול הרחבות
    from routes.auth import auth_bp
    from routes.users import users_bp
    from routes.events import events_bp
    from routes.content import content_bp
    from routes.news import news_bp
    from routes.uploads import uploads_bp
    from routes.image import image_bp
    from routes.email import email_bp # <--- ייבוא ה-Blueprint החדש (ודא שזה email_bp.py)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(content_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(uploads_bp)
    app.register_blueprint(image_bp)
    app.register_blueprint(email_bp, url_prefix='/api') # <--- רישום Blueprint חדש

    @app.route("/")
    def index():
        return "Flask server is running"
    
    # הקונטקסט של האפליקציה נוצר אוטומטית ב-flask run,
    # אבל אם אתה מריץ python app.py, זה חשוב שיהיה מחוץ ל-create_app
    # או שתוודא ש-create_all() נקרא בתוך קונטקסט
    # עם זאת, עדיף ש-db.create_all() יקרה בתוך app.run() או בפקודת CLI ייעודית.
    # נשאיר את זה ב-if __name__ == '__main__': בלבד.
    # with app.app_context():
    #     db.create_all()
            
    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context(): # <--- זה עדיין חשוב אם אתה מריץ כך
        db.create_all()
    app.run(debug=True)

