from datetime import datetime
from flask import jsonify, request
from app import api, db
from app.database.models import Order, Product
from sqlalchemy import desc

#CRD
@api.route('/order', methods=['GET'])
def get_orders():
    return jsonify([o.to_dict() for o in Order.query.all()])


@api.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    return jsonify(Order.query.get_or_404(id).to_dict())


@api.route('/order', methods=['POST'])
def create_order():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({'success': False, 'message': 'Invalid or missing JSON'}), 400

    if not all(k in data for k in ('user_id', 'price', 'products')):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    order = Order(
        user_id=data['user_id'],
        price=data['price']
    )

    product_ids = data['products']
    products = Product.query.filter(Product.id.in_(product_ids)).all()

    if len(products) != len(product_ids):
        return jsonify({'success': False, 'message': 'One or more products not found'}), 404

    order.products.extend(products)

    db.session.add(order)
    db.session.commit()

    return jsonify(order.to_dict()), 201


@api.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted'})


@api.route('/order/check', methods=['GET'])
def order_check():
    user_id = request.args.get('user_id', type=int)

    if not user_id:
        return jsonify({'success': False, 'message': 'user_id parameter is required'}), 400

    last_order = (
        db.session.query(Order)
        .filter(Order.user_id == user_id, Order.delivered_at == None)
        .order_by(desc(Order.created_at))
        .first()
    )

    if last_order:
        return jsonify({'order': last_order.to_dict()})
    else:
        return jsonify({'order': None})
    
@api.route('/order/deliver', methods=['POST'])
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