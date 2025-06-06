from datetime import datetime
from app import api, db
from app.database.models import User, Role
from flask import jsonify, request
import bcrypt

@api.route("/users")
def get_users():
    email = request.get_json(force=True)['email']
    if email:
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({'message': 'User not found'}), 404
    else:
        return jsonify([u.to_dict() for u in User.query.all()])


@api.route("/users/<int:id>")
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@api.route("/users", methods=['POST'])
def create_user():
    data = request.get_json(force=True)

    if not all(k in data for k in ('name', 'email', 'password')):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({'success': False, 'message': 'Email already exists'}), 409

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    user = User(
        name=data['name'],
        email=data['email'],
        password=hashed_password
    )

    user.roles.append(Role.query.filter_by(name = 'client').first())
    db.session.add(user)
    db.session.commit()

    return jsonify({'success': True, 'data': user.to_dict()}), 201


@api.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json(force=True)
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    user.password = data.get("password", user.password)
    user.updated_at = datetime.now()
    db.session.commit()
    return jsonify(user.to_dict())


@api.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({ "message": "User deleted" })