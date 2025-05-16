from app import app
from app.database.models import User
from flask import request, jsonify
import jwt


def auth(f):
    def inner():
        auth_header = request.headers.get('Authorization', '')
        auth_parts = auth_header.split()

        if len(auth_parts) != 2:
            return jsonify({
                'success': False,
                'message': 'No token provided, access denied'
            }), 401

        try:
            token = auth_parts[1]
            data = jwt.decode(token, app.secret_key, ["HS256", "HMAC"])
            user = User.query.filter_by(email = data['email']).first()
            if user:
                return jsonify({ 'success': True, 'data': user, 'message': 'pong' })
            return jsonify({ 'success': False, 'message': 'Wrong email' })
        except jwt.ExpiredSignatureError:
            return jsonify({ 'success': False, 'message': 'Token expired' })
        except (jwt.InvalidTokenError, Exception) as ex:
            return jsonify({ 'success': False, 'message': 'Invalid token', 'ex': ex.args })
    return inner
