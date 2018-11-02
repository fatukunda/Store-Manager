from flask import Blueprint, request, Response, jsonify
from app.models.product import Product
from app.models.sale import Sale
from app.controllers import sale_controller
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import search_sales_person

bp = Blueprint('sales_view', __name__, url_prefix='/api/v1')


""" SALE ROUTES"""

@bp.route('/sales')
@jwt_required
def get_sales():
        # Get all sales by the admin
        return jsonify(sale_controller.get_all_sales())


@bp.route('/sales/<sale_id>')
@jwt_required
def get_a_single_sale(sale_id):
        """ Get sale details"""
        current_user = get_jwt_identity()
        sales_person = search_sales_person(current_user)
        if sales_person['user_type'] == 'admin':
                if sale_controller.get_sale_details(sale_id):
                        return jsonify(sale_controller.get_sale_details(sale_id))
                else:
                        return jsonify({"message": "Sale Item with an Id of {} was not found".format(sale_id)}), 404
        else:
                return jsonify({"message": "Not authorized to access this route"})

@bp.route('attendants/<attendant_id>/sales')
@jwt_required
def get_attendant_sales(attendant_id):
        # Get all sales made by a particular store attendant

        return jsonify(sale_controller.get_all_sales(attendant_id))

@bp.route('/sales', methods=['POST'])
@jwt_required
def make_sale():
    # Attendant make a sale
    request_data = request.get_json()
    sold_item = request_data['sold_item']
    quantity_sold = request_data['quantity_sold']
    sales_person = get_jwt_identity()
    seller = search_sales_person(sales_person)
    if quantity_sold == 0:
        return jsonify({"message": "Please enter a number above zero"})
    if seller['user_type'] == 'admin':
        return jsonify({"message": "Only sale attendants can make sales"})
    else:
            sale_controller.make_a_sale(sold_item, sales_person, quantity_sold)
            return jsonify({"message" : "Sale successfully completed"}), 201
    


