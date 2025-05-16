from datetime import datetime
from app import api, db, bcrypt
from app.database.models import User
from flask import jsonify, request

@api.route("/user", methods=["GET"])
def get_users():
    return jsonify([u.to_dict() for u in User.query.all()])

@api.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@api.route("/user", methods=['POST'])
def create_user():
    data = request.get_json(force=True)

    if not all(k in data for k in ('name', 'email', 'password')):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'success': False, 'message': 'Email already exists'}), 409

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'success': True, 'data': user.to_dict()}), 201


@api.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)
    user.updated_at = datetime.now()
    db.session.commit()
    return jsonify(user.to_dict())

@api.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({ "message": "User deleted" })