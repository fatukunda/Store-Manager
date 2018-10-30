# app/__init__.py
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from app.views import sales_view
from app.views import users_view
from app.views import products_view
from app.views import auth_view
from app.db.config_db import create_tables
from configparser import ConfigParser
import yaml


app = Flask(__name__, instance_relative_config=True)
 # Register the products_view bluprint
app.register_blueprint(sales_view.bp)
#Register the sales_view blueprint
app.register_blueprint(users_view.bp)
# Register the products view
app.register_blueprint(products_view.bp)
""" Register authentication view"""
app.register_blueprint(auth_view.bp)

app.config['JWT_SECRET_KEY'] = 'Code-Benders'
jwt = JWTManager(app)

# filename = os.path.join('app' , 'config.yml')
# with open(filename) as f:
#     config = f.read()
#     config = yaml.load(config)
#     for key, value in config.items():
#         print(key)
#         app.config()
create_tables()