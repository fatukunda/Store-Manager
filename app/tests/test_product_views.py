from flask import request,jsonify, json
import pytest
from app.models.products import products
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
# test GET/api/v1/products
def test_get_products_returns_all_products(client):
    with client:
        res = client.get('/api/v1/products')
        assert res.status_code == 200
        assert json_of_response(res)
        
# test GET/api/v1/products/<id>    
def test_get_single_product_returns_a_product(client):
    with client:
        res = client.get('/api/v1/products/<id>')
        assert res.status_code == 200
        assert json_of_response(res)
        assert len(json_of_response(res)) == 1