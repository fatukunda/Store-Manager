from app.db.config_db import connect
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import execute
class Auth:
    role = ''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.set_password(password)

    # def set_password(self, password):
    #     self.pw_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     check_password_hash(self.pw_hash, password)
