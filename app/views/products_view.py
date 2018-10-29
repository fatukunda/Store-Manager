from flask import Blueprint, request, Response, jsonify,json
from app.models.product import Product
from app.views import create_store
from app.models.sale import Sale

bp = Blueprint('products_view', __name__, url_prefix='/api/v1/products')

store = create_store()

""" PRODUCT ROUTES"""
# Add a product to the inventory
@bp.route('', methods=['POST'])
def add_product():
    product = Product()
    request_data = request.get_json()
    product.name = request_data['name']
    product.category = request_data['category']
    product.quantity = request_data['quantity']
    product.price = request_data['price']
    product.in_stock = request_data['in_stock']
    product.create_product()
    # store.create_product(product.name, product.category, product.quantity, product.price, product.in_stock)
    return Response('Product %s created successfully' % product.name, status=201)

""" Delete a specific product"""
@bp.route('/<product_id>', methods =['DELETE'])
def delete_product(product_id):
    rows_deleted = Product.delete_product(product_id)
    if rows_deleted > 0:
        return 'Product deleted successfully'

""" Edit a specific product"""
@bp.route('/<product_id>', methods =['PUT'])
def edit_product(product_id):
    request_data = request.get_json()
    name = request_data['name']
    category = request_data['category']
    quantity = request_data['quantity']
    price = request_data['unit_price']
    in_stock = request_data['in_stock']
    product = Product.edit_product(product_id, name, category, quantity, price, in_stock)
    return product

# Get all products in the store
@bp.route('/', methods= ['GET'])
def get_products():
        return jsonify(Product.get_all_products())

# Get a single product
@bp.route('/<product_id>')
def get_single_product(product_id):
        product = Product.search_single_product(product_id)
        if product:
                return jsonify(product)
        else:
                Response('Product with an Id of '+ product_id + 'was not found', status=404)
