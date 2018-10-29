from flask import Blueprint, request, Response, jsonify
from app.models.product import Product
from app.views import create_store
from app.models.sale import Sale

bp = Blueprint('sales_view', __name__, url_prefix='/api/v1/sales')


store = create_store()

""" SALE ROUTES"""
# Get all sales by the admin
@bp.route('/')
def get_sales():
    return jsonify(store.get_all_sales())

# Get a single sale by admin
@bp.route('/<id>')
def admin_get_single_sale(id):
   pass

# Get all sales made by a particular store attendant
@bp.route('/<attendant_id>/sales')
def attendant_get_sales(attendant_id):
    pass

# Get a single sale made by a specific attendant
@bp.route('/<attendant_id>/sales/<sale_id>')
def get_single_sale(attendant_id, sale_id):
    pass


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
