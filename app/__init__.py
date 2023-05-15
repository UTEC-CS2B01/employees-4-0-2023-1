from flask import Flask
from .models import db, setup_db
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        setup_db(app)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Max-Age', '15')
        return response


    return app

