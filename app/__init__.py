from flask import (
    Flask,
    request,
    jsonify,
    abort,
)
from .models import db, setup_db, Employee
from .utils.utilities import allowed_file
from flask_cors import CORS
import os
import sys

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
        error_code = 200
        list_errors = []
        try:
            body = request.form

            if 'first_name' not in body:
                list_errors.append('first_name is required')
            else:
                first_name = request.form.get('first_name')

            if 'last_name' not in body:
                list_errors.append('last_name is required')
            else:
                last_name = request.form.get('last_name')

            if 'job_title' not in body:
                list_errors.append('job_title is required')
            else:
                job_title = request.form.get('job_title')

            if 'selectDepartment' not in body:
                list_errors.append('selectDepartment is required')
            else:
                department_id = request.form.get('selectDepartment')

            if 'image' not in request.files:
                print('image is required')
                list_errors.append('image is required')
            else:
                file = request.files['image']

                if file.filename == '':
                    list_errors.append('filename should not be empty')
                
                if not allowed_file(file.filename):
                    list_errors.append('File extension not allowed')
            

            if len(list_errors) > 0:
                error_code = 400
            else:
                employee = Employee(first_name, last_name, job_title, department_id)
                db.session.add(employee)
                db.session.commit()
                employeeid_created = employee.id
                
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
        except Exception as e:
            db.session.rollback()
            print("e: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            error_code = 500

        if error_code == 400:
            return jsonify({'success': False, 'message': 'Error creating employee', 'errors': list_errors}), error_code
        elif error_code == 500:
            return jsonify({'success': False, 'message': 'Internal Server Error'}), error_code
        else:
            return jsonify({'success': True, 'id': employeeid_created, 'message': 'Employee created successfully'}), 201


    @app.route('/employees', methods=['GET'])
    def get_employees():
        employees = Employee.query.filter_by(is_active=True).order_by(Employee.first_name).all()
        return jsonify({'success': True, 'employees': [e.serialize() for e in employees]}), 200



    return app

