from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from extensions import db
from flask_migrate import Migrate
import json

from dotenv import load_dotenv
import os 

load_dotenv()  

def create_app():


    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # לדוגמה, תיקייה בשם 'uploads' בתיקיית העבודה הנוכחית
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
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
    app = Flask(__name__)
    
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    app.config.from_pyfile('config.py')
    
    migrate = Migrate(app, db)

    db.init_app(app)

    from routes.auth import auth_bp
    from routes.users import users_bp
    from routes.events import events_bp
    from routes.content import content_bp
    from routes.news import news_bp
    
    app.register_blueprint(news_bp)
    app.register_blueprint(content_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(events_bp)

   
    with app.app_context():
        db.create_all()
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
