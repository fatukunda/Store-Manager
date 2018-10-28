import psycopg2

def connect():
    conn = psycopg2.connect(database='store-manager-db', user='postgres', password='admin')

    cursor = conn.cursor()
    return cursor