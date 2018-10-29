# app/__init__.py
from flask import Flask
from app.views import admin_views
from app.views import attendants_views
from app.db.config_db import create_tables

app = Flask(__name__, instance_relative_config=True)
 # Register the products_view bluprint
app.register_blueprint(admin_views.bp)
#Register the sales_view blueprint
app.register_blueprint(attendants_views.bp)
create_tables()