from app import api, app
from app.database.models import User
from app.decorators import auth
from app.utils import get_auth_token
from flask import request, jsonify
from datetime import datetime, timezone, timedelta
import jwt
import bcrypt

@api.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email = data['email']).first()
    if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
        token = jwt.encode({
            'sub': user.email,
            'iat': datetime.now(timezone.utc),  # Specify timezone, timezone has to be imported
            'exp': datetime.now(timezone.utc) + timedelta(days=30)
            },
            app.config['SECRET_KEY']
        )
        return jsonify({
            'success': True,
            'token': token,
            'user': user.to_dict()
        })
    return jsonify({
        'success': False,
        'message': 'No user with that email'
    }), 401

@api.route('/user')
@auth
def get_auth_user():
    data = jwt.decode(get_auth_token(), app.secret_key, ["HS256", "HMAC"])
    user = User.query.filter_by(email = data['sub']).first()

    return user.to_dict()