import psycopg2

TEST_DATABASE_CONFIG = {
    'host': 'localhost',
    'db_name': 'store_manager_test_db',
    'user': 'postgres',
    'password': 'admin',
    'port': 5432
}
DATABASE_CONFIG = {
    'host': 'localhost',
    'db_name': 'store_manager_db',
    'user': 'postgres',
    'password': 'admin',
    'port': 5432
}

def connect(db_name):
    if db_name != DATABASE_CONFIG['db_name']:
        raise ValueError("Couldn't not find DB with given name")
    conn = psycopg2.connect(database=DATABASE_CONFIG['db_name'], 
    user=DATABASE_CONFIG['user'],
     password=DATABASE_CONFIG['password'])
  
    return conn

"""commit changes to the database and close connection"""
def commit_to_db(conn, cursor):
    conn.commit()
    cursor.close()
    if conn is not None:
        conn.close()

def create_tables():
    """ create tables in the store_manager_db"""
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
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
    connection = connect('store_manager_db')
    cursor = connection.cursor()
    for command in commands:
        cursor.execute(command)
    commit_to_db(connection, cursor)
  