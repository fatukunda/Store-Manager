from flask import json
from flask_jwt_extended import create_access_token
import pytest
from app.models.product import Product
from app.controllers import product_controller
from app import app
from app.models.sale import Sale
from urllib.request import urlopen

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


# Helper methods

def json_response(response):
    """Covert response to json"""
    res =  json.loads(response.data.decode('utf8'))
    return [res]

# test GET/api/v1/products
# def test_get_products_returns_all_products(client):
#     with app.app_context():
#         access_token = create_access_token('user')
#         headers = {
#                 'Authorization': 'Bearer {}'.format(access_token)
#         }
#         res = client.get('/api/v1/products', headers = headers)
#         assert res.status_code == 200
#         assert json_response(res)

# test GET/api/v1/products/<id>    
def test_get_single_product_returns_a_product(client):
    with app.app_context():
        access_token = create_access_token('user')
        headers = {
                'Authorization': 'Bearer {}'.format(access_token)
        }
        product_id = 3
        res = client.get('/api/v1/products/{}'.format(product_id), headers = headers)
        assert res.status_code == 200
        assert json_response(res)
        
# Test POST/api/v1/products
def test_add_product_adds_a_product(client):    
    with app.app_context():
            access_token = create_access_token('admin')
            headers = {
                    'Authorization': 'Bearer {}'.format(access_token)
            }
            product = Product('Laptops', 'Toshiba laptop', 6, 2000000)
            number_of_products_before = len(product_controller.get_all_products())
            res = client.post('/api/v1/products', data =json.dumps(dict(
                    name = product.name,
                    category = product.category,
                    quantity = product.quantity,
                    unit_price = product.price,
                    in_stock = product.in_stock
                    
            )), content_type='application/json', headers = headers)
            number_of_products_after = len(product_controller.get_all_products())
            assert res.status_code ==201
            assert number_of_products_after > number_of_products_before
            assert product_controller.get_all_products()[-1] in product_controller.get_all_products()



        
            
