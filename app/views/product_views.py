# product_views.py
import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products, Product

bp = Blueprint('product_views', __name__, url_prefix='/api/v1')

# Helper methods
def get_product_given_param(parameter):
    product_list = []
    for product in products:
        [product_list.append(product) for key in product if product[key] == parameter]
    return jsonify(product_list)

# Get all products in the store
@bp.route('/products', methods= ['GET'])
def get_products():
    if len(products) > 0:
        return jsonify(products)
    else:
        return jsonify({
            'message': 'No products found. Please add some products'
        })

# Get a single product
@bp.route('/products/<id>')
def get_single_product(id):
    if len(products) > 0:
        return get_product_given_param(id)
    else:
        return 'No products were found'
  

# Add a product to the inventory
@bp.route('admin/products', methods=['POST'])
def add_product():
    product = Product()
    product.name = request.form.get('name')
    product.category = request.form.get('category')
    product.quantity = request.form.get('quantity')
    product.price = request.form.get('price')
    product_details = {
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'quantity': product.quantity,
        'price': product.price
    }
    products.append(product_details)
    return 'Product %s created successfully' % product.name