import psycopg2
import os
from app.config import set_config

def connect():
    conn = psycopg2.connect(host = 'ec2-184-73-199-189.compute-1.amazonaws.com', database='dektsfu001hn6g', user='plwlxtobexznlo', password='752178d58b5ffaebe1e11a9000136b77d76035f5dea0d2c82926236f2dcd2385')
    return conn
    # conn = None
    # if set_config['test']:
    #     conn = psycopg2.connect(database = 'store_manager_test_db', user ='postgres', password='admin')
        
    # elif set_config['prod']:
    #     conn = psycopg2.connect(host = 'ec2-54-225-98-131.compute-1.amazonaws.com', database='d1bp4lvbptrsc4', user='akhgvtysmhhqdx', password='d712e55fb1572068657cca43da19638b5676f338ef2313c1fdcb880b37e51c13')
    # else:
    #     conn = psycopg2.connect(database = 'store_manager_db', user ='postgres', password='admin')

    # return conn

# def create_admin_user(conn):
#     sql = """INSERT INTO users(first_name, last_name, username, email, password, user_type)
#                  VALUES('Frank', 'Atukunda', 'fatukunda', 'admin@app.com', 'admin123', 'admin');"""
#     cursor = conn.cursor()
#     cursor.execute(sql)

def commit_to_db(conn, cursor):
    """commit changes to the database and close connection"""
    conn.commit()
    cursor.close()
    if conn is not None:
        conn.close()

def create_tables(conn):
    """ create tables in the store_manager_db"""
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL,
            category VARCHAR(255) NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price FLOAT NOT NULL,
            in_stock BOOLEAN NOT NULL
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                username VARCHAR(255) UNIQUE NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                user_type VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE IF NOT EXISTS sales (
                sale_id SERIAL PRIMARY KEY,
                sales_person_id INTEGER NOT NULL,
                sale_date DATE NOT NULL,
                quantity_sold INTEGER NOT NULL,
                product_sold_id INTEGER NOT NULL,
                total_price FLOAT NOT NULL,
                FOREIGN KEY (sales_person_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (product_sold_id)
                    REFERENCES products (product_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    # connection = connect()
    cursor = conn.cursor()
    for command in commands:
        cursor.execute(command)
    commit_to_db(conn, cursor)
  