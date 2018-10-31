from werkzeug.security import generate_password_hash, check_password_hash
from app.db.config_db import connect, commit_to_db
from app.models import execute
class User:
    first_name = '',
    last_name = ''
    role = 'user'
    def __init__(self, username = '', email = '', password =''):
        self.username = username
        self.email = email
        self.password = password
        
