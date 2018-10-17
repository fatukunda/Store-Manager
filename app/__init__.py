# app/__init__.py
import os

from flask import Flask
from app.views import product_views
from app.views import sales_views


def create_app(test_config=None):
    #Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY ='dev'
    )
    if test_config is None:
    #Load the instance config, if it exists when testing
        app.config.from_pyfile('config.py', silent=True)
    else:
    #Load the test config if passed in
        app.config.from_mapping(test_config)
    #Ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Register the products_view bluprint
    app.register_blueprint(product_views.bp)
    #Register the sales_view blueprint
    app.register_blueprint(sales_views.bp)

    return app
