import uuid
from flask import Blueprint, request, Response, jsonify
from app.models.sale import Sale
from app.views import create_store
from time import ctime

#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')
store = create_store()
def get_attendant(username):
    pass
    # for attendant in attendants:
    #    [attendant for key in attendant if attendant[key] == username]

# Get all sales by the admin
@bp.route('/admin/sales')
def get_sales():
    return jsonify(store.get_all_sales())

# Get a single sale by admin
@bp.route('/admin/sales/<id>')
def admin_get_single_sale(id):
   pass

# Get all sales made by a particular store attendant
@bp.route('attendants/<username>/sales')
def attendant_get_sales(username):
    pass

# Get a single sale made by a specific attendant
@bp.route('/attendants/<username>/sales/<id>')
def attendant_get_single_sale(username, id):
    get_attendant(username)
    pass


# Attendant make a sale
@bp.route('/attendants/<attendant_id>/sales', methods=['POST'])
def make_sale(attendant_id):
    sale = Sale()
    request_data = request.get_json()
    sale.sales_person = attendant_id
    sale.sold_item = request_data['sold_item']
    sale.quantity_sold = request_data['quantity_sold']

    store.create_sale(attendant_id, sale.date, sale.quantity_sold, sale.sold_item, sale.total_price)
    return Response('Sale %s made successfully' % sale.sold_item, status=201) 
