from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_TOKEN_LOCATION'] = 'cookies'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super-secret'
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)
app.config["JWT_CSRF_METHODS"] = []

jwt = JWTManager(app)
db = SQLAlchemy(app)

from app.models import *
from app.utils import init_status_db

with app.app_context():
    db.create_all()
    init_status_db(db)


from app.views import *
from app import routes
