# product_views.py
import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products

bp = Blueprint('product_views', __name__, url_prefix='/api/v1')

@bp.route('/products', methods= ['GET'])
def get_products():
    return jsonify(products)
# Add a new product
@bp.route('admin/products', methods=['POST'])
def add_product():
    name = request.form.get('name')
    category = request.form.get('category')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    product = {
        'id': str(uuid.uuid4()),
        'name': name,
        'category': category,
        'quantity': int(quantity),
        'price': float(price)
    }
    products.append(product)
    return 'Product %s created successfully' % product['name']