from werkzeug.security import generate_password_hash, check_password_hash
from app.db.config_db import connect, commit_to_db
class User:
    first_name = '',
    last_name = ''
    role = 'user'
    def __init__(self, username = '', email = '', password =''):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def create_user(self):
        """ insert a new user into the user table """
        sql = """INSERT INTO users(first_name, last_name, username, email, password, user_type)
                 VALUES(%s, %s, %s, %s, %s, %s) RETURNING user_id, first_name, last_name, username, email, password, user_type;"""
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (self.first_name, self.last_name, self.username, self.email, self.set_password, self.role))
        user = cursor.fetchone()
        commit_to_db(conn, cursor)
        return user