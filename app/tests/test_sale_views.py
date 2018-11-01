from flask import json
from flask_jwt_extended import create_access_token
import pytest
from app.controllers import sale_controller
from app import app
from app.models.sale import Sale
""" SALES TESTS"""

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def json_response(response):
    """Covert response to json"""
    res =  json.loads(response.data.decode('utf8'))
    return [res]

# Test GET/api/v1/sales
def test_make_sale(client):
    with app.app_context():
            username = 'luke'
            sales_person_id = 10
            item_to_sale = 1
            access_token = create_access_token(username)
            headers = {
                    'Authorization': 'Bearer {}'.format(access_token)
            }
            sale = Sale(sales_person_id, item_to_sale, 2)
            number_of_sales_before = len(sale_controller.get_all_sales())
            res = client.post('/api/v1/sales', data =json.dumps(dict(
                    sales_person_id = sale.sales_person,
                    sale_date = sale.date,
                    quantity_sold = sale.quantity_sold,
                    sold_item = sale.sold_item
            )), content_type='application/json', headers = headers)
            number_of_sales_after = len(sale_controller.get_all_sales())
            assert res.status_code ==201
            assert number_of_sales_after > number_of_sales_before
            assert sale_controller.get_all_sales()[-1] in sale_controller.get_all_sales()

# Test GET/api/v1/sales/<sale_id>    
def test_get_single_sale_returns_a_sale(client):
    with app.app_context():
        access_token = create_access_token('user')
        headers = {
                'Authorization': 'Bearer {}'.format(access_token)
        }
        sale_id = 1
        res = client.get('/api/v1/products/{}'.format(sale_id), headers = headers)
        assert res.status_code == 200