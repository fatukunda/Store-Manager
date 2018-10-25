import uuid

class Attendant:
    first_name = ''
    last_name = ''
    email = ''
    def __init__(self, username='',user_type='user', id = str(uuid.uuid4())):
        self.username = username
        self.user_type = user_type
        self.id = id

# Dummy list of attendants

attendants = [
    {
    'id': str(uuid.uuid4()),
    'first_name': 'Simon',
    'last_name': 'Lee',
    'email': 'lee@store.com',
    'username': 'simonLee',
    'user_type': 'user'
    },
    {
    'id': str(uuid.uuid4()),
    'first_name': 'Paul',
    'last_name': 'Ryan',
    'email': 'ryan@store.com',
    'username': 'pRyan',
    'user_type': 'user'
    },
    {
    'id': str(uuid.uuid4()),
    'first_name': 'Jane',
    'last_name': 'Logan',
    'email': 'logan@store.com',
    'username': 'jLogan',
    'user_type': 'user'
    }
]