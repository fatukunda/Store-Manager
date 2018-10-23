# product_views.py
import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products, Product
from app.utils import search, get_collection

bp = Blueprint('product_views', __name__, url_prefix='/api/v1')

# Get all products in the store
@bp.route('/products', methods= ['GET'])
def get_products():
    return get_collection(products)

# Get a single product
@bp.route('/products/<id>')
def get_single_product(id):
    if len(products) > 0:
        return  search(id, products)
  

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