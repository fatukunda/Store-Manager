from app.db.config_db import commit_to_db, connect
from app.models import execute

def create_user(first_name, last_name, username, email, password, role):
        """ insert a new user into the user table """
        sql = """INSERT INTO users(first_name, last_name, username, email, password, user_type)
                 VALUES(%s, %s, %s, %s, %s, %s) RETURNING user_id, first_name, last_name, username, email, password, user_type;"""
        conn = connect('store_manager_db')
        cursor = conn.cursor()
        cursor.execute(sql, (first_name, last_name, username, email, password, role))
        user = cursor.fetchone()
        commit_to_db(conn, cursor)
        return user

def get_all_users():
    """ Get all the users in the users table"""
    sql = """ SELECT * FROM users;"""
    conn = connect('store_manager_db')
    cursor = execute(sql)
    users = cursor.fetchall()
    user_list = []
    for user in users:
        user_details = {
            'user_id': user['user_id'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'username': user['username'],
            'email': user['email'],
            'role': user['user_type']
        }
        user_list.append(user_details)
    commit_to_db(conn, cursor)
    return user_list


def get_user_details(user_id):
    sql =  "SELECT * FROM users WHERE user_id = '{0}'".format(user_id)
    conn = connect('store_manager_db')
    cursor = execute(sql)
    user = cursor.fetchone()
    commit_to_db(conn, cursor)
    return user

def give_admin_rights(user_id, role):
    sql = "SELECT * FROM users WHERE user_id = '{}'".format(user_id)
    sql2 = "UPDATE users SET user_type = '{}'".format(role)
    conn = connect('store_manager_db')
    cursor = execute(sql)
    user = cursor.fetchone()
    if user[6] != role:
        cursor.execute(sql2)
        commit_to_db(conn, cursor)
        return user
    else:
        return 'User already Administrator'

def delete_attendant(attendant_id):
    sql = "DELETE FROM users WHERE user_id = {0};".format(attendant_id)
    rows_deleted = 0
    cursor = execute(sql)
    rows_deleted = cursor.rowcount
    return rows_deleted