from flask import request,jsonify, json
import pytest
from app.models.products import products
from app import app

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def post_json(client, url, json_dict):
    """Send dictionary json_dict as a json to the specified url """
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))

def test_get_products_returns_all_products(client):
    with client:
        res = client.get('/api/v1/products')
        assert res.status_code == 200
        