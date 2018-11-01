from app.db.config_db import connect
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import execute

class Auth:
    """Authentication model"""
    table = 'users'
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __dict__(self):
        """
	    Should be defined so that object can 
		be serialized, in this case to JSON
		"""
        return { 'username': self.username, 'password': self.password}

    def login(self, sql):
        cursor = execute(sql)
        user = cursor.fetchone()
        return user

