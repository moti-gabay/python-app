from flask_mail import Mail
from flask_cors import CORS
from flask_pymongo import PyMongo

mongo = PyMongo()
mail = Mail()
cors = CORS()
