from flask import jsonify
from app import app
from app.models import Product
from app.constants import API_PREFIX

@app.route(f"{API_PREFIX}/buy/<id>")
def buy_product(id = None):
    if not id:
        return jsonify("id param is required"), 400
    products = Product.query.filter_by(id = id).get()
    if not products:
        return jsonify("no product with that id found"), 404
    return products[0].to_dict()