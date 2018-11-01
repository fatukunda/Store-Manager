from flask import Blueprint, request, Response, jsonify
from app.models.product import Product
from app.models.sale import Sale
from app.controllers import sale_controller

bp = Blueprint('sales_view', __name__, url_prefix='/api/v1')


""" SALE ROUTES"""
@bp.route('/sales')
def get_sales():
        # Get all sales by the admin
        return jsonify(sale_controller.get_all_sales())


@bp.route('/sales/<sale_id>')
def get_a_single_sale(sale_id):
        """ Get sale details"""
        if sale_controller.get_sale_details(sale_id):
                return jsonify(sale_controller.get_sale_details(sale_id))
        else:
                return jsonify({"message": "Sale Item with an Id of {} was not found".format(sale_id)}), 404

@bp.route('attendants/<attendant_id>/sales')
def get_attendant_sales(attendant_id):
        # Get all sales made by a particular store attendant
        return jsonify(sale_controller.get_all_sales(attendant_id))


@bp.route('/attendants/<attendant_id>/sales/<sale_id>')
def get_single_sale(attendant_id, sale_id):
        # Get a single sale made by a specific attendant
        pass


# Attendant make a sale
@bp.route('/sales', methods=['POST'])
def make_sale():
    request_data = request.get_json()
    sold_item = request_data['sold_item']
    quantity_sold = request_data['quantity_sold']
    sales_person = request_data['sales_person_id']
    if sale_controller.make_a_sale(sold_item, sales_person, quantity_sold):
            return jsonify({"message" : "Sale successfully completed"}), 201
    else:
            return jsonify({"message": "There are no sales made yet"})    

