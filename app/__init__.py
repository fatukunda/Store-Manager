# app/__init__.py
from flask import Flask
from flask_jwt_extended import JWTManager
from app.views import sales_view
from app.views import users_view
from app.views import products_view
from app.views import auth_view
from app.db.config_db import create_tables
from app.config import set_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(set_config[config_name])
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
    create_tables()
    print(config_name)

    return app