from werkzeug.security import generate_password_hash, check_password_hash
from app.db.config_db import connect, commit_to_db
class User:
    first_name = '',
    last_name = ''
    role = 'user'
    def __init__(self, username = '', email = '', password =''):
        self.username = username
        self.email = email
        self.password = password

    def create_user(self):
        """ insert a new user into the user table """
        sql = """INSERT INTO users(first_name, last_name, username, email, password, user_type)
                 VALUES(%s, %s, %s, %s, %s, %s) RETURNING user_id, first_name, last_name, username, email, password, user_type;"""
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (self.first_name, self.last_name, self.username, self.email, generate_password_hash(self.password), self.role))
        user = cursor.fetchone()
        commit_to_db(conn, cursor)
        return user

    @staticmethod
    def get_all_users():
        """ Get all the users in the users table"""
        sql = """ SELECT * FROM users;"""
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        users = cursor.fetchall()
        user_list = []
        for user in users:
            user_details = {
                'user_id': user[0],
                'first_name': user[1],
                'last_name': user[2],
                'username': user[3],
                'email': user[4],
                'user_type': user[6]
            }
            user_list.append(user_details)
        commit_to_db(conn, cursor)
        return user_list

    @staticmethod
    def get_user_details(user_id):
        sql =  "SELECT * FROM users WHERE user_id = '{0}'".format(user_id)
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        user_details = {
            'user_id': user[0],
            'first_name': user[1],
            'last_name': user[2],
            'username': user[3],
            'email': user[4],
            'user_type': user[6]
            }
        commit_to_db(conn, cursor)
        return user_details

    @staticmethod    
    def give_admin_rights(user_id, role):
        sql = "SELECT * FROM users WHERE user_id = '{}'".format(user_id)
        sql2 = "UPDATE users SET user_type = '{}'".format(role)
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        user = cursor.fetchone()
        if user[6] != role:
            cursor.execute(sql2)
            commit_to_db(conn, cursor)
            return user
        else:
            return 'User already Administrator'
        
