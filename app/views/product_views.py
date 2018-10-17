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
=======
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

