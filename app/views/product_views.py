# product_views.py
import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products

bp = Blueprint('product_views', __name__, url_prefix='/api/v1')

# Get all products in the store
@bp.route('/products', methods= ['GET'])
def get_products():
    return jsonify(products)

#Get a single product details
@bp.route('/products/<id>')
def get_single_product(id):
    product_list = []
    for product in products:
        for key in product:
            if product[key] == id:
                product_list.append(product)
    return jsonify(product_list)