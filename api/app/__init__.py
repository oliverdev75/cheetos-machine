from flask import Flask, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import timedelta
from dotenv import load_dotenv
from .constants import API_PREFIX
from .database.DatabaseConfig import DatabaseConfig
import os
import secrets

# This function is called just below library imports to load all app configuration
load_dotenv()

app = Flask(__name__)
api = Blueprint('api', __name__, url_prefix=API_PREFIX)

# Just allows requests from frontend management server,
# By default Flask doesn't allow requests from other hosts
CORS(
    app,
    resources={r"/api/*": {"origins": "*"}},
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    supports_credentials=False
)

@app.before_request
def log_headers():
    print(f"{request.method} {request.path} headers: {dict(request.headers)}")


@app.after_request
def add_cors_headers(res):
    res.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return res

db_config = DatabaseConfig(
    type=os.getenv('DB_CONNECTION'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    name=os.getenv('DB_NAME'),
)

app.config.update(
    SECRET_KEY=secrets.token_hex(16),
    SESSION_PERMANENT=True,
    PERMANENT_SESSION_LIFETIME=timedelta(days=31),
    SQLALCHEMY_DATABASE_URI=db_config.get_string()
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .database.models import User, Role, Product, Order
from . import console

from .routes import *

app.register_blueprint(api)