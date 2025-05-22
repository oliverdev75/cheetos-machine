from app import api, app
from app.database.models import User
from flask import request, jsonify
from datetime import datetime, timezone, timedelta
import jwt

@api.route("login", methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email = data['email'], password = data['password']).first()
    if user:
        token = jwt.encode({
            'sub': user.email,
            'iat': datetime.now(timezone.utc),  # Specify timezone, timezone has to be imported
            'exp': datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            app.config['SECRET_KEY']
        )
        return jsonify({
            'success': True,
            'token': token,
        })
    return jsonify({
        'success': False,
        'message': 'No user with that email'
    }), 401