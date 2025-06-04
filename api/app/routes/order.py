from datetime import datetime
from flask import jsonify, request
from app import api, db, app
from app.database.models import Order, Product, User
from app.utils import get_auth_token
from sqlalchemy import desc
import jwt

#CRD
@api.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([o.to_dict() for o in Order.query.all()])


@api.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    return jsonify(Order.query.get_or_404(id).to_dict())


@api.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json(force=True)

    if not data:
        return jsonify({'success': False, 'message': 'Invalid or missing JSON'}), 400

    if 'product' not in data:
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
    
    auth_data = jwt.decode(get_auth_token(), app.secret_key, ["HS256", "HMAC"])
    user = User.query.filter_by(email = auth_data['sub']).first()
    user.tokens = user.tokens - data['product']['tokens']
    db.session.commit()
    order = Order(
        user_id=user.id,
        tokens=data['product']['tokens'],
    )

    order.products.append(Product.query.get_or_404(data['product']['id']))
    db.session.add(order)
    db.session.commit()

    return jsonify([order.to_dict(), user.to_dict()]), 201


@api.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted'})


@api.route('/orders/check', methods=['GET'])
def order_check():

    last_order = (
        db.session.query(Order)
        .filter(Order.delivered_at == None)
        .order_by(desc(Order.created_at))
        .first()
    )

    if last_order:
        return jsonify({'order': last_order.to_dict()})
    else:
        return jsonify({'order': None})
    
@api.route('/orders/deliver', methods=['POST'])
def deliver_last_order():
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'user_id is required'}), 400

    # Buscar el último pedido sin entregar de ese usuario
    last_order = (
        Order.query
        .filter(Order.user_id == user_id)
        .order_by(desc(Order.created_at))
        .first()
    )

    if not last_order:
        return jsonify({'success': False, 'message': 'No pending orders found for this user'}), 404

    # Asignar la fecha actual
    last_order.delivered_at = datetime.utcnow()
    db.session.commit()

    return jsonify({'success': True, 'message': 'Order marked as delivered', 'order': last_order.to_dict()})