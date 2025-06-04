from datetime import datetime
from flask import jsonify, request, send_file
from app import api, db
from app.database.models import Product
from app.decorators import auth

@api.route("/buy/<id>", methods=["GET"])
@auth
def buy_product(id = None):
    if not id:
        return jsonify("id param is required"), 400
    products = Product.query.filter_by(id = id).get()
    if not products:
        return jsonify("no product with that id found"), 404
    return products[0].to_dict()


@api.route('/products', methods=['GET'])
@auth
def get_products():
    print("authed!!!!")
    return jsonify([p.to_dict() for p in Product.query.all()])


# GET - Get product by ID
@api.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    return jsonify(Product.query.get_or_404(id).to_dict())


@api.route('/products/image/<int:id>')
def get_product_image(id):
    product = Product.query.filter_by(id = id).first_or_404()
    return send_file(f"images/{product.image}.png", mimetype='image/jpeg')

# POST - Create product
@api.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(
        name=data['name'],
        price=data['price'],
        image=data['image']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201


# PUT - Update product by ID
@api.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.image = data.get('image', product.image)
    product.updated_at = datetime.now()
    db.session.commit()
    return jsonify(product.to_dict())


# DELETE - Delete product by ID
@api.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({ 'message': 'Product deleted' })