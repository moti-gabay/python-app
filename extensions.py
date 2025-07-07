# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail # ייבוא Flask-Mail

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
mail = Mail() # אתחול Flask-Mail
