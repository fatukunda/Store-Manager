from app.db.config_db import connect
class Auth:
    role = ''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        sql =  "SELECT * FROM users WHERE username = '{0}' and password = '{1}'".format(self.username, self.password)
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        return user