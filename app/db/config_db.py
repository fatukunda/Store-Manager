import psycopg2

def connect():
    """ Connect to the database """
    conn = None
    try:
        conn = psycopg2.connect(database='store-manager-db', user='postgres', password='admin')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn

"""commit changes to the database and close connection"""
def commit_to_db(conn, cursor):
    conn.commit()
    cursor.close()
    if conn is not None:
        conn.close()

def create_tables():
    """ create tables in the store-manager-db"""
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS products (
            product_id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price FLOAT NOT NULL,
            in_stock BOOLEAN NOT NULL
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS users (
                user_id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
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
                sale_id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
                sales_person_id uuid NOT NULL,
                sale_date DATE NOT NULL,
                quantity_sold INTEGER NOT NULL,
                product_sold_id uuid NOT NULL,
                total_price FLOAT NOT NULL,
                FOREIGN KEY (sales_person_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (product_sold_id)
                    REFERENCES products (product_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    connection = connect()
    cursor = connection.cursor()
    for command in commands:
        cursor.execute(command)
    commit_to_db(connection, cursor)
  