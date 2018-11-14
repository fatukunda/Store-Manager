# app/__init__.py
import psycopg2
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from app.views import sales_view
from app.views import users_view
from app.views import products_view
from app.views import auth_view
from app.db.config_db import create_tables
from app.config import set_config
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(set_config[config_name])
     # Register the products_view bluprint
    app.register_blueprint(sales_view.bp)
    #Register the sales_view blueprint
    app.register_blueprint(users_view.bp)
    # Register the products view
    app.register_blueprint(products_view.bp)
    """ Register authentication view"""
    app.register_blueprint(auth_view.bp)
    # app.config['JWT_SECRET_KEY'] = 'Code-Benders'
    jwt = JWTManager(app)
    CORS(products_view.bp)

    
    conn = None
    if config_name == 'prod':
        conn = psycopg2.connect(host = 'ec2-184-73-199-189.compute-1.amazonaws.com', database='dektsfu001hn6g', user='plwlxtobexznlo', password='752178d58b5ffaebe1e11a9000136b77d76035f5dea0d2c82926236f2dcd2385')
    elif config_name == 'test':
        conn = psycopg2.connect(database = 'store_manager_test_db', user ='postgres', password='admin')
    else:
        conn = psycopg2.connect(database = 'store_manager_db', user ='postgres', password='admin')
    
    create_tables(conn)

    return app