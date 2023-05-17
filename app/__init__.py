from flask import (
    Flask,
    request,
    jsonify
)
from .models import db, setup_db, Employee
from .utils.utilities import allowed_file
from flask_cors import CORS
import os

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'static/employees'
    with app.app_context():
        setup_db(app)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Max-Age', '15')
        return response
    
    @app.route('/employees', methods=['POST'])
    def create_employee():
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        job_title = request.form.get('job_title')
        department_id = request.form.get('selectDepartment')

        if 'image' not in request.files:
            return jsonify({'success': False, 'message': 'No image provided'}), 400
        
        file = request.files['image']

        if file.filename == '':
            return jsonify({'success': False, 'message': 'No image provided'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'success': False, 'message': 'File extension not allowed'}), 400
        

        employee = Employee(first_name, last_name, job_title, department_id)
        db.session.add(employee)
        db.session.commit()
        
        cwd = os.getcwd()

        employee_dir = os.path.join(app.config['UPLOAD_FOLDER'], employee.id)
        os.makedirs(employee_dir, exist_ok=True)

        upload_folder = os.path.join(cwd, employee_dir)

        absolute_path = os.path.join(upload_folder, file.filename)
        file.save(absolute_path)
        file.close()

        relative_path = os.path.join(employee_dir, file.filename)

        employee.image_path = relative_path
        db.session.commit()

        return jsonify({'success': True, 'id': employee.id, 'message': 'Employee created successfully'}), 201


    return app

