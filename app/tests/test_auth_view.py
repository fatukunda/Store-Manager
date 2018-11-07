from flask import json
import pytest
from app import create_app
from app.models.auth import Auth

app = create_app('test')

@pytest.fixture
def client():
    client = app.test_client()
    yield client

def test_login_returns_access_for_registered_users(client):
    with app.app_context():
        user = 'fatukunda'
        user_pass = 'admin123'
        auth = Auth(user, user_pass)
        res = client.post('/api/v1/auth/login', data = json.dumps(dict(
            username = auth.username,
            password = auth.password
        )),content_type='application/json')
        assert res.status_code == 200