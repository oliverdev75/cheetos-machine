from app import app
from app.database.models import User
from flask import request, jsonify
import jwt


def auth(f):
    def wrapper():
        auth_header = request.headers.get('Authorization', '')
        auth_parts = auth_header.split()
        data = None
        try:
            token = auth_parts[1]
            data = jwt.decode(token, app.secret_key, ["HS256"])
            user = User.query.filter_by(email = data['sub']).first()
            if user:
                return f()
            return jsonify({ 'success': False, 'message': 'Wrong email' }), 401
        except jwt.ExpiredSignatureError:
            return jsonify({ 'success': False, 'message': 'Token expired' }), 401
        except (jwt.InvalidTokenError) as ex:
            return jsonify({ 'success': False, 'message': 'Invalid token', 'ex': ex.args }), 401
    wrapper.__name__ = f.__name__
    return wrapper
