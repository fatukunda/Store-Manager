# product_views.py
import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products, Product

bp = Blueprint('product_views', __name__, url_prefix='/api/v1')

# Get all products in the store
@bp.route('/products', methods= ['GET'])
def get_products():
    return jsonify(products)

# Get a single product
@bp.route('/products/<id>')
def get_single_product(id):
    product_list = []
    for product in products:
        for key in product:
            if product[key] == id:
                product_list.append(product)
    return jsonify(product_list)

# Add a product to the inventory
@bp.route('admin/products', methods=['POST'])
def add_product():
    name = request.form.get('name')
    category = request.form.get('category')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    product = Product(name, category, quantity, price)
    product_details = {
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'quantity': int(product.quantity),
        'price': float(product.price)
    }
    products.append(product_details)
    return 'Product %s created successfully' % product.name