# views.py

from flask import Flask

from app import app

@app.route('/')
def index():
    return 'Hello Flask'