import uuid
from flask import Flask, Blueprint, request, Response
from app.models.sales import sales, Sale
from app.models.attendant import attendants
from app.utils import search, get_collection

#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')

def get_attendant(username):
    for attendant in attendants:
       [attendant for key in attendant if attendant[key] == username]

# Get all sales by the admin
@bp.route('/admin/sales')
def get_sales():
    return get_collection(sales)


# Get a single sale by admin
@bp.route('/admin/sales/<id>')
def admin_get_single_sale(id):
   return search(id, sales)

# Get all sales made by a particular store attendant
@bp.route('attendants/<username>/sales')
def attendant_get_sales(username):
    return search(username, sales)

# Get a single sale made by a specific attendant
@bp.route('/attendants/<username>/sales/<id>')
def attendant_get_single_sale(username, id):
    get_attendant(username)
    return search(id, sales)


# Attendant make a sale
@bp.route('/attendants/<username>/sales', methods=['POST'])
def make_sale(username):
    sale = Sale()
    request_data = request.get_json()
    sale.sales_person = username
    sale.sold_item = request_data['sold_item']
    sale.quantity_sold = request_data['quantity_sold']
    sale.unit_price = request_data['unit_price']
    sale.total_price = request_data['total_price']
    saleInfo = {
        'date':sale.date,
        'id': sale.id,
        'quantity_sold': sale.quantity_sold,
        'sales_person': sale.sales_person,
        'sold_item': sale.sold_item,
        'total_price': sale.total_price,
        'unit_price':sale.unit_price
    }
    sales.append(saleInfo)
    return Response('Sale %s made successfully' % sale.sold_item, status=201) 
