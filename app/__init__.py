from flask import (
    Flask,
    request,
    jsonify,
    abort,
)
from .models import db, setup_db, Employee, Department
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
    
    @app.route('/employees/<employee_id>', methods=['PATCH'])
    def update_employee(id):
        employee = Employee.query.get(id)
        formulario = request.form
        if employee is None:
            return jsonify({'success': False, 'message': 'No se encuentra empleado'}), 404
        
        else:
            if 'first_name' in formulario:
                employee.first_name = formulario['first_name']
            if 'last_name' in formulario:
              employee.last_name = formulario['last_name']
            if 'job_title' in formulario:
              employee.job_title = formulario['job_title']
            if 'selectDepartment' in formulario:
              employee.deparment_id = formulario['selectDepartment']
            
        db.session.commit()

        return jsonify({'success': True, 'message': 'Los datos del empleado se actualizaron correctamente'}), 200

    @app.route('/employees/<id>', methods=['DELETE'])
    def delete_employee(id):
        employee = Employee.query.get(id)
        
        if employee is None:
            return jsonify({'success': False, 'message': 'No se encuentra empleado'}), 404
        
        else:
            db.session.delete(employee)
            db.session.commit()
            return  jsonify({'success': True, 'message': 'Se eliminó el empleado'}), 200
         

    @app.route('/department', methods=['GET'])
    def get_departments():
        departments = Department.query.order_by(Department.short_name).all()
        return jsonify({'success': True, 'departments': [e.serialize() for e in departments]}), 200

    @app.route('/departments', methods=['POST'])
    def create_department():
        errors = []
        try:
            
            formulario = request.form
            if 'name' not in formulario:
                errors.append('name is required')
            else:
                name = formulario.get('name')

            if 'short_name' not in formulario:
                errors.append('short_name is required')
            else:
                short_name = formulario.get('short_name')

            if len(errors) > 0:
                error_code = 400
            else:
                department = Department(name, short_name)
                db.session.add(department)
                db.session.commit()

        except Exception as e:
            db.session.rollback()
            print("e: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            error_code = 500

        if error_code==400:
            return jsonify({'success': False, 'message': 'Error creating department', 'errors': errors}), error_code
        elif error_code==500:
            return jsonify({'success': False, 'message': 'Internal Server Error'}), error_code
        else:
            return jsonify({'success': True, 'id': department.id, 'name':department.name, 'short_name':department.short_name ,'message': 'Department created successfully'})
    
    @app.route('/departments/<id>', methods=['PATCH'])
    def update_department(id):
        department = Department.query.get(id)
        formulario = request.form
        if department is None:
            return jsonify({'success': False, 'message': 'No se encuentra el departamento'}), 404
        
        else:
            if 'name' in formulario:
                department.name = formulario['name']
            if 'short_name' in formulario:
                department.short_name = formulario['short_name']
            if 'created_at' in formulario:
                department.created_at = formulario['created_at']
            
            
        db.session.commit()

        return jsonify({'success': True, 'message': 'Los datos del departamento se actualizaron correctamente'}), 200


    @app.route('/departments/<id>', methods=['DELETE'])
    def delete_department(id):
        department = Department.query.get(id)
        if department is None:
            return jsonify({'success': False, 'message': 'No se encuentra el departamento'}), 404
        else:
            db.session.delete(department)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Departamento eliminado exitosamente'})
    
    @app.route('/departments/<id>', methods=['SEARCH'])
    def search_department(id):
        department = Department.query.get(id)
        if department is None:
            return jsonify({'success': False, 'message': 'No se encuentra el departamento'})
        else:
            return jsonify({'id': department.id, 'name': department.name, 'short_name': department.short_name})
           
    @app.route('/employees/<id>', methods=['SEARCH'])
    def search_employee(id):
        employee = Employee.query.get(id)
        if employee is None:
            return jsonify({'success': False, 'message': 'No se encuentra el empleado'})
        else:
            return jsonify({
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'job_title': employee.job_title,
            'created_at': employee.created_at,
            'modified_at': employee.modified_at,
            'image_path': employee.image_path,
            'is_active': employee.is_active,
            'department_id': employee.department_id})
        
    return app
    
