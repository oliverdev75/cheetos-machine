from app import app
from app.database.models import User
from flask import request
import jwt

def get_auth_token():
    auth_header = request.headers.get('Authorization', '')
    auth_parts = auth_header.split()

    return auth_parts[1]