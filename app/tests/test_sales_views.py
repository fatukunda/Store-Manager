from flask import request, json
import pytest
from app.models.sales import sales, Sale
from app import app
import uuid

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


# Helper methods
def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    res =  json.loads(response.data.decode('utf8'))
    return [res]

# Test GET/api/v1/admin/sales
def test_get_sales_returns_all_sales(client):
    with client:
        res = client.get('/api/v1/admin/sales')
        assert res.status_code == 200
        assert json_of_response(res)

# Test GET/api/v1/admin/sales/<id>    
def test_get_single_sale_returns_a_sale(client):
    with client:
        res = client.get('/api/v1/admin/sales/<id>')
        assert res.status_code == 200
        assert json_of_response(res)
        assert len(json_of_response(res)) == 1
# Test GET/api/v1/attendants/<username>/sales
def test_attendant_get_sales(client):
    with client:
        res = client.get('/api/v1/attendants/<username>/sales')
        assert res.status_code == 200
        assert json_of_response(res)

# Test GET/api/v1/attendants/<username>/sales/<id>
def test_get_single_sale_for_attendant(client):
    with client:
        res = client.get('/api/v1/attendants/<username>/sales/<id>')
        assert res.status_code == 200
        assert json_of_response(res)
        assert len(json_of_response(res)) == 1


# def test_add_product_adds_a_product(client):
#     product = Product('17 inch Toshiba Laptop', 'Laptops', 10, 1600000.00)
#     with client:
#         number_of_products = len(products)
#         res = client.post('api/v1/admin/products', data = json.dumps(dict(
#             id = product.id,
#             name = product.name,
#             category = product.category,
#             quantity = product.quantity,
#             price = product.quantity

#         )) , content_type ='application/json')
#         assert product.id in products[3]['id']
#         assert res.status_code == 200
#         assert len(products) > number_of_products
        
            
