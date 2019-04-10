import waitress
from flask import Flask, render_template, request, url_for, redirect

from app.products import Product, ProductManager

import os


def start():
    app = Flask(__name__)

    manager = ProductManager()

    jacket = Product(name='Куртка', vendor_code=1234560, size=42, price=7000, number=1, selling=False)
    skirt = Product(name='Юбка', vendor_code=1234561, size=44, price=3000, number=1, selling=False)
    trousers = Product(name='Брюки', vendor_code=1234562, size=42, price=5000, number=1, selling=True)
    dress = Product(name='Платье', vendor_code=1234563, size=40, price=10000, number=1, selling=True)


    # product = Product(name, vendor_code, size, price, number, selling=False)

    manager.add(jacket)
    manager.add(skirt)
    manager.add(trousers)
    manager.add(dress)


    @app.route('/')
    def index():
        availability = manager.availability()
        return render_template('index.html', availability=availability)

    @app.route('/sales')
    def sale():
        sales = manager.sales()
        return render_template('sale.html', sales=sales)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9871, debug=True)


if __name__ == '__main__':
    start()
