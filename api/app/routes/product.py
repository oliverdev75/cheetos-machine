from flask import jsonify
from app import api
from app.database.models import Product
from app.constants import API_PREFIX

@api.route("/buy/<id>")
def buy_product(id = None):
    if not id:
        return jsonify("id param is required"), 400
    products = Product.query.filter_by(id = id).get()
    if not products:
        return jsonify("no product with that id found"), 404
    return products[0].to_dict()