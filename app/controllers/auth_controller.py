from app.models.auth import Auth
from app.models import execute

def login(username, password):
    sql =  "SELECT user_id, username, password, user_type FROM users WHERE username = '{0}' AND password = '{1}';".format(username, password)
    cursor = execute(sql)
    user = cursor.fetchone()
    return user

    