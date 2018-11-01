from app.models.auth import Auth
from app.models import execute

def login(username, password):
    sql =  "SELECT username, password, user_type FROM users WHERE username = '{0}';".format(username)
    cursor = execute(sql)
    user = cursor.fetchone()
    print(user)
    return user

    