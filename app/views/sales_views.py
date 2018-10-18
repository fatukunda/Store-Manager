import uuid
from flask import Flask, Blueprint, request, jsonify, json
from app.models.products import products
from app.models.sales import sales, Sale
from app.models.attendant import attendants


#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')

# Get all sales by the admin
@bp.route('/admin/sales')
def get_sales():
    if len(sales) > 0:
        return jsonify(sales)
    else:
        return 'No sales found'

# Get a single sale by admin
@bp.route('/admin/sales/<id>')
def admin_get_single_sale(id):
    sale_list = []
    for sale in sales:
        for key in sale:
            if sale[key] == id:
                sale_list.append(sale)
    return jsonify(sale_list)

# Get all sales made by a particular store attendant
@bp.route('attendants/<username>/sales')
def attendant_get_sales(username):
    sale_list = []
    for sale in sales:
        for key in sale:
            if sale[key] == username:
                sale_list.append(sale)
    return jsonify(sale_list)

# Get a single sale made by a specific attendant
@bp.route('/attendants/<username>/sales/<id>')
def attendant_get_single_sale(username, id):
    sale_list = []
    for attendant in attendants:
        for key in attendant:
            if attendant[key] == username:
                for sale in sales:
                    for key in sale:
                        if sale[key] == id:
                            sale_list.append(sale)
    return jsonify(sale_list)


# Attendant make a sale
@bp.route('/attendants/<username>/sales', methods=['POST'])
def make_sale(username):
    for attendant in attendants:
        for key in attendant:
            if attendant[key] == username:
                sold_item = request.form.get('sold_item')
                quantity_sold = request.form.get('quantity_sold')
                unit_price = request.form.get('unit_price')
                total_price = request.form.get('total_price')
                sale = Sale(attendant['username'], sold_item, quantity_sold, total_price, unit_price)
                saleInfo = {
                    'date':sale.date,
                    'id': sale.id,
                    'quantity_sold':int(sale.quantity_sold),
                    'sales_person': sale.sales_person,
                    'sold_item': sale.sold_item,
                    'total_price':float(sale.total_price),
                    'unit_price':float(sale.unit_price)
                }
                sales.append(saleInfo)
    return 'Sale successfully made'