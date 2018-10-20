import uuid
from flask import Flask, Blueprint, request, jsonify, json
from app.models.products import products
from app.models.sales import sales, Sale
from app.models.attendant import attendants


#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')

def get_sales_given_param(parameter):
    sale_list = []
    for sale in sales:
        [sale_list.append(sale) for key in sale if sale[key] == parameter]
    return jsonify(sale_list)

def get_attendant(username):
    for attendant in attendants:
       return [attendant for key in attendant if attendant[key] == username]

# Get all sales by the admin
@bp.route('/admin/sales')
def get_sales():
    if len(sales) > 0:
        return jsonify(sales)
    else:
        return jsonify({'message': 'No sales found'})


# Get a single sale by admin
@bp.route('/admin/sales/<id>')
def admin_get_single_sale(id):
   return get_sales_given_param(id)

# Get all sales made by a particular store attendant
@bp.route('attendants/<username>/sales')
def attendant_get_sales(username):
    return get_sales_given_param(username)

# Get a single sale made by a specific attendant
@bp.route('/attendants/<username>/sales/<id>')
def attendant_get_single_sale(username, id):
    if(get_attendant(username)):
        return get_sales_given_param(id)


# Attendant make a sale
@bp.route('/attendants/<username>/sales', methods=['POST'])
def make_sale(username):
    sale = Sale()
    sale.sales_person = username
    sale.sold_item = request.form.get('sold_item')
    sale.quantity_sold = request.form.get('quantity_sold')
    sale.unit_price = request.form.get('unit_price')
    sale.total_price = request.form.get('total_price')
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
    return 'Sale %s made successfully' % sale.sold_item
