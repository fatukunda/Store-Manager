from app.models.auth import Auth

def login(username, password):
    auth = Auth(username, password)
    sql =  "SELECT username, password, user_type FROM users WHERE username = '{}';".format(auth.username)
    user  = auth.login(sql)
    return user

    