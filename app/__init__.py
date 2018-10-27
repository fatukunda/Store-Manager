# app/__init__.py
# import psycopg2
# from flask import Flask

# # local import
# from instance.config import app_config

# # initialize database
# # db = psycopg2.connect(database='store-manager-db', user='admin', password='admin')

from flask import Flask
from app.views import admin_view
from app.views import attendant_view
from app.models.store import Store

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(admin_view.bp)
app.register_blueprint(attendant_view.bp)