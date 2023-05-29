from flask import (
    Flask,
    request,
    jsonify
)

from .models import db, setup_db, Producto, Categoria
from flask_cors import CORS
from utilities.utils import allowed_file

import os
import sys

def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        app.config['UPLOAD_FOLDER'] = 'static/employees'
        setup_db(app)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        response.headers.add(' Access-Control-Max-Age', '10')
        return response

    #### Categories ####

    @app.route('/categories', methods=['POST'])
    def create_category():

        pass

    @app.route('/categories', methods=['GET'])
    def get_categories():
        


        pass

    @app.route('/categories/<category_id>', methods=['PATCH'])
    def update_category(category_id):
        pass

    @app.route('/categories/<category_id>', methods=['DELETE'])
    def delete_category(category_id):

         category = Categoria.query.get(category_id)
         if category is None:
            return jsonify({'success': False, 'message': 'No se encuentra la categoria'}), 404
         else:
            db.session.delete(category)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Categoria eliminada exitosamente'})
    pass

    #### Products ####

    @app.route('/products', methods=['POST'])
    def create_product():
        pass

    @app.route('/products', methods=['GET'])
    def get_products():
        try:
            search_query = request.args.get('query', None)
            if search_query:
                products = Producto.query.filter(Producto.name.ilike(f'%{search_query}%')).order_by(Producto.name).all()
                return jsonify({'succes':True, 'employees': [e.serialize() for e in products]}), 200
        except Exception as e:
            print("e: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()
            return jsonify({'succes':False, 'products': 'Internal Server Error'}), 500

        pass

    @app.route('/products/<product_id>', methods=['PATCH'])
    def update_product(product_id):
        product = Producto.query.get(product_id)
        form = request.form
        try:
         if product is None:
            return jsonify({'success': False, 'message': 'No se encuentra producto'}), 404
        
         else:
            if 'fname' in form:
                Producto.name = form['name']
            if 'price' in form:
                Producto.price = form['price']
            if 'job_title' in form:
                Producto.stock = form['stock']
            if 'selectDepartment' in form:
                Producto.category_id = form['category_id']
            return jsonify({'success': True, 'message': 'Los datos del producto se actualizaron correctamente'}), 200
        
        except Exception as e:
            print("e: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()
            return jsonify({'succes':False, 'products': 'Internal Server Error'}), 500
    
    
        pass

    @app.route('/products/<product_id>', methods=['DELETE'])
    def delete_product(product_id):
        
        product = Producto.query.get(product_id)
        
        if product is None:
            return jsonify({'success': False, 'message': 'No se encuentra producto'}), 404
        
        else:
            db.session.delete(product)
            db.session.commit()
            return  jsonify({'success': True, 'message': 'Se eliminó producto'}), 200
    pass


    return app
