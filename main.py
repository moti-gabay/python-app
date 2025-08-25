from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db, migrate, mail, cors
import os
from dotenv import load_dotenv

load_dotenv()  # טען משתני סביבה

def create_app():
    app = Flask(__name__)  # אתחול Flask

    # תיקיות להעלאות
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    IMAGES_UPLOAD_FOLDER = 'uploaded_images'
    os.makedirs(IMAGES_UPLOAD_FOLDER, exist_ok=True)

    # משתני סביבה
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("DB_DRIVER")  # לדוגמה: "ODBC Driver 18 for SQL Server"

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

    # הגדרות Flask
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['IMAGES_UPLOAD_FOLDER'] = IMAGES_UPLOAD_FOLDER

    # הגדרות Flask-Mail
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() in ['true','1','t']
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

    # אתחול הרחבות
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})
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

    @app.route("/", methods=["GET"])
    def index():
        return "Flask server is running"

    return app


# 🔹 הוספת משתנה app ברמת המודול עבור Gunicorn
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
