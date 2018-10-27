from flask import jsonify, Blueprint, Response, abort, request
from app.views.admin_view import store
from app.shared import search
from app.models.sale import Sale

bp = Blueprint('attendant_view', __name__, url_prefix='/api/v1/attendants')

""" User panel"""
@bp.route('/<attendant_id>')
def user_panel(attendant_id):
    attendant = search(attendant_id, store.sales_attendants)
    if attendant:
        return 'Welcome ' + attendant_id + ' to your panel'
    else:
        return Response('Attendant ' + attendant_id + ' not found', status=404)

""" Get a list of sales for a given attendant"""
@bp.route('/<attendant_id>/sales', methods=['GET'])
def get_attendant_sales(attendant_id):
    attendant = search(attendant_id, store.sales_attendants)
    if attendant:
        attendant = attendant[0]
        return jsonify(attendant['sales_made'])
    else:
        return Response('No such attendant', status=404)

@bp.route('/<attendant_id>/sales', methods=['POST'])
def make_a_sale(attendant_id):
    attendant = search(attendant_id, store.sales_attendants)
    if attendant:
        attendant = attendant[0]
        request_data = request.get_json()
        new_sale_details = {
            'sold_item': request_data['sold_item'],
            'quantity_sold': request_data['quantity_sold']
        }
        sale = store.make_a_sale(new_sale_details['sold_item'], new_sale_details['quantity_sold'], attendant)
        if sale:
            return 'Sale made successfully'
        else:
            return Response('Product is out of stock')
    else:
        return Response('No such attendant', status=404)
        