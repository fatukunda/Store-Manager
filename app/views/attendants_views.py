# product_views.py
from flask import Blueprint, request, Response, jsonify
from app.models.product import Product
from app.models.sale import Sale
from app.views import create_store

bp = Blueprint('product_views', __name__, url_prefix='/api/v1/store')

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

# Attendant make a sale
@bp.route('/<attendant_id>/sales', methods=['POST'])
def make_sale(attendant_id):
    sale = Sale()
    request_data = request.get_json()
    sale.sales_person = attendant_id
    sale.sold_item = request_data['sold_item']
    sale.quantity_sold = request_data['quantity_sold']

    store.create_sale(attendant_id, sale.date, sale.quantity_sold, sale.sold_item, sale.total_price)
    return Response('Sale %s made successfully' % sale.sold_item, status=201) 

""" Get sale details"""
@bp.route('/<attendant_id>/sales/<sale_id>')
def get_a_single_sale(sale_id):
        pass
