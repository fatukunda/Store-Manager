# app/__init__.py
from flask import Flask
from app.views import product_views
from app.views import sales_views

app = Flask(__name__, instance_relative_config=True)
 # Register the products_view bluprint
app.register_blueprint(product_views.bp)
#Register the sales_view blueprint
app.register_blueprint(sales_views.bp)



if __name__ == '__main__':
   app.run(debug=True)