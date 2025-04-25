from flask import Flask, request, jsonify
import jwt
import secrets
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()

user = { 'email': 'test@demo.com', 'name': 'Test user', 'alias': 'testuser' }

@app.route('/')
def index():
    return "<h1>Hello Flask!</h1>"

@app.route('/api/ping')
def ping():
    auth_header = request.headers.get('Authorization', '')
    print(f"Authorization header: {auth_header!r}")
    auth = auth_header.split()

    print(f"auth list: {auth}")
    if len(auth) != 2:
        return jsonify({
            'success': False,
            'message': 'No token provided, access denied'
        }), 401

    try:
        token = auth[1]
        data = jwt.decode(token, app.secret_key, ["HS256", "HMAC"])

        if user['email'] == data['sub']:
            return jsonify({ 'success': True, 'data': user, 'message': 'pong' })
        return jsonify({ 'success': False, 'message': 'Wrong email' })
    except jwt.ExpiredSignatureError:
        return jsonify({ 'success': False, 'message': 'Token expired' })
    except (jwt.InvalidTokenError, Exception) as ex:
        return jsonify({ 'success': False, 'message': 'Invalid token', 'ex': ex.args })
    
@app.route('/login', methods=['POST'])
def login():
    print(datetime.now())
    print(datetime.utcnow())
    data = request.get_json()
    if data['email'] == user['email']:
        token = jwt.encode({
            'sub': user['email'],
            'iat': datetime.now(timezone.utc),  # Especificar la zona horaria, timezone hay que importarlo
            'exp': datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            app.secret_key,
        )
        return jsonify({
            'success': True,
            'token': token,
        })
    return jsonify({
        'success': False,
        'message': 'Bad email'
    }), 401