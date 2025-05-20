from datetime import datetime
from flask import jsonify, request
from app import api, db
from app.database.models import Order

#CRD
@api.route('/order', methods=['GET'])
def get_orders():
    return jsonify([o.to_dict() for o in Order.query.all()])


@api.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    return jsonify(Order.query.get_or_404(id).to_dict())


@api.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()

    if not all(k in data for k in ('user_id', 'price')):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    order = Order(
        user_id=data['user_id'],
        price=data['price']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201


@api.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted'})
