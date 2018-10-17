import uuid
from flask import Flask, Blueprint, request, jsonify
from app.models.products import products

#  Set up a blueprint for the sales views
bp = Blueprint('sales_views', __name__, url_prefix='/api/v1')