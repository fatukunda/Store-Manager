# product_views.py
from flask import Blueprint, request, Response, jsonify
from app.models.products import Product
from app.views import create_store

bp = Blueprint('product_views', __name__, url_prefix='/api/v1')

store = create_store()
# Get all products in the store
@bp.route('/products', methods= ['GET'])
def get_products():
        return jsonify(store.get_all_products())

# Get a single product
@bp.route('/products/<product_id>')
def get_single_product(product_id):
        product = store.search_single_product(product_id)
        if product:
                return jsonify(product)
        else:
                Response('Product with an Id of '+ product_id + 'was not found', status=404)
  

# Add a product to the inventory

@bp.route('admin/products', methods=['POST'])
def add_product():
    product = Product()
    request_data = request.get_json()
    product.name = request_data['name']
    product.category = request_data['category']
    product.quantity = request_data['quantity']
    product.price = request_data['price']
    product.in_stock = request_data['in_stock']
    
    store.create_product(product.name, product.category, product.quantity, product.price, product.in_stock)
    return Response('Product %s created successfully' % product.name, status=201)