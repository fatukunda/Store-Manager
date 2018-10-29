# app/__init__.py
from flask import Flask
from app.views import sales_view
from app.views import attendants_view
from app.views import products_view
from app.db.config_db import create_tables

app = Flask(__name__, instance_relative_config=True)
 # Register the products_view bluprint
app.register_blueprint(sales_view.bp)
#Register the sales_view blueprint
app.register_blueprint(attendants_view.bp)
# Register the products view
app.register_blueprint(products_view.bp)
create_tables()