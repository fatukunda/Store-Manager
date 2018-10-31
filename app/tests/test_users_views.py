from flask import json
from flask_jwt_extended import create_access_token
import pytest
from app.controllers import user_controller
from app import app
from app.models.user import User

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

# test GET/api/v1/attendants
# def test_get_attendants_returns_all_attendants(client):
#     with app.app_context():
#         access_token = create_access_token('admin')
#         headers = {
#                 'Authorization': 'Bearer {}'.format(access_token)
#         }
#         res = client.get('/api/v1/attendants', headers = headers)
#         assert res.status_code == 200
#         assert json_response(res)

# Test GET/api/v1/attendants/<id>    
def test_get_single_attendant_returns_an_attendant(client):
    with app.app_context():
        access_token = create_access_token('admin')
        headers = {
                'Authorization': 'Bearer {}'.format(access_token)
        }
        attendant_id = 5
        res = client.get('/api/v1/attendants/{}'.format(attendant_id), headers = headers)
        assert res.status_code == 200
        assert json_response(res)
        
# Test POST/api/v1/attendants
def test_add_attendant_adds_an_attendant(client):    
    with app.app_context():
            access_token = create_access_token('admin')
            headers = {
                    'Authorization': 'Bearer {}'.format(access_token)
            }
            attendant = User('matty', 'samatm@app.com', 'my_pass123')
            attendant.first_name = 'Martin'
            attendant.last_name = "Mikes"
            attendant.role = 'user'
            number_of_attendants_before = len(user_controller.get_all_users())
            res = client.post('/api/v1/attendants', data =json.dumps(dict(
                    first_name = attendant.first_name,
                    last_name = attendant.last_name,
                    username = attendant.username,
                    password = attendant.password,
                    email = attendant.email,
                    role = attendant.role
                    
            )), content_type='application/json', headers = headers)
            number_of_attendants_after = len(user_controller.get_all_users())
            assert res.status_code ==201
            assert number_of_attendants_after > number_of_attendants_before
            assert user_controller.get_all_users()[-1] in user_controller.get_all_users()

            
