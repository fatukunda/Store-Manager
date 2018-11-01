from flask import json
from flask_jwt_extended import create_access_token
import pytest
from app import app
from app.models.auth import Auth

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_login_returns_access_for_registered_users(client):
    with app.app_context():
        user = 'kamau'
        user_pass = 'kamau1'
        auth = Auth(user, user_pass)
        res = client.post('/api/v1/auth/login', data = json.dumps(dict(
            username = auth.username,
            password = auth.password
        )),content_type='application/json')
        assert res.status_code == 200