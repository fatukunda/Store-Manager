import pytest
from flask import json
from flask_jwt_extended import create_access_token
from app.models.product import Product
from app.controllers import product_controller
from app import create_app

app = create_app('test')

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


def test_add_product_adds_a_product(client):
    with app.app_context():
            access_token = create_access_token(100)
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
                    
            )), content_type='application/json', headers = headers)
            number_of_products_after = len(product_controller.get_all_products())
            assert res.status_code ==201
            assert number_of_products_after > number_of_products_before
            assert product_controller.get_all_products()[-1] in product_controller.get_all_products()

 
def test_get_single_product_returns_a_product(client):
        # test GET/api/v1/products/<id>   
    with app.app_context():
        access_token = create_access_token('user')
        headers = {
                'Authorization': 'Bearer {}'.format(access_token)
        }
        product_id = 4
        res = client.get('/api/v1/products/{}'.format(product_id), headers = headers)
        assert res.status_code == 200
        assert json_response(res)


def test_get_products_returns_all_products(client):
        # Test GET/api/v1/products
    with app.app_context():
        access_token = create_access_token('user')
        headers = {
                'Authorization': 'Bearer {}'.format(access_token)
        }
        res = client.get('/api/v1/products/', headers = headers)
        assert res.status_code == 200
        assert json_response(res)

def test_admin_can_edit_a_product(client):
        with app.app_context():
                access_token = create_access_token(100)
                headers = {
                    'Authorization': 'Bearer {}'.format(access_token)
                }
                product_id = 3
                quantity = 20
                unit_price = 24000000
                res = client.put('/api/v1/products/{}'.format(product_id), data = json.dumps (dict(
                        quantity = quantity,
                        unit_price = unit_price
                )), content_type ='application/json', headers = headers)
                assert res.status_code == 200
                product = product_controller.search_a_product(product_id)
                assert product['unit_price'] == unit_price
                assert product['quantity'] == quantity

def test_admin_can_delete_a_product(client):
        with app.app_context():
                access_token = create_access_token(100)
                headers = {
                    'Authorization': 'Bearer {}'.format(access_token)
                }   
                product_id = 30
                res = client.delete('/api/v1/products/{}'.format(product_id), headers = headers)
                assert res.status_code == 200
                product = product_controller.search_a_product(product_id)
                assert not product

