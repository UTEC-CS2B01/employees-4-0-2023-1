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
        setup_db(app, test_config['database_qa'] if test_config else None)
        CORS(app, origins='*')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        response.headers.add('Access-Control-Max-Age', '15')
        return response
    
    @app.route('/employees', methods=['POST'])
    def create_employee():
        error_code = 201
        list_errors = []
        try:
            body = request.form

            if 'first_name' not in body:
                list_errors.append('first_name is required')

            if 'last_name' not in body:
                list_errors.append('last_name is required')

            if 'job_title' not in body:
                list_errors.append('job_title is required')

            if 'selectDepartment' not in body:
                list_errors.append('selectDepartment is required')

            if 'image' not in request.files:
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
                employee_id_created = employee.id

                cwd = os.getcwd()

                employee_dir = os.path.join(app.config['UPLOAD_FOLDER'], str(employee_id_created))
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
            print("e:", e)
            return jsonify({'success': False, 'message': 'Error creating employee', 'errors': list_errors}), 400

        if error_code == 400:
            return jsonify({'success': False, 'message': 'Error creating employee', 'errors': list_errors}), error_code
        elif error_code != 201:
            abort(error_code)
        else:
            return jsonify({
                'success': True,
                'id': employee_id_created,
                'first_name': first_name,
                'last_name': last_name,
                'job_title': job_title,
                'message': 'Employee created successfully'
            }), 201


    @app.route('/employees', methods=['GET'])
    def get_employees():
        
        try:
            search_query = request.args.get('query', None)
            if search_query:
                employees = Employee.query.filter_by(is_active=True).filter(Employee.first_name.ilike('%{}%'.format(search_query)))\
                    .order_by(Employee.first_name).all()
                
                return jsonify({'success': True, 'employees': [e.serialize() for e in employees], 'total': len(employees)}), 200

            employees = Employee.query.filter_by(is_active=True).order_by(Employee.first_name).all()
            return jsonify({'success': True, 'employees': [e.serialize() for e in employees]}), 200
        except Exception as e:
            print("e: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Internal Server Error'}), 500

    @app.route('/employees/<id>', methods=['PATCH'])
    def update_employee(id):
        returned_code = 200
        try:
            employee = Employee.query.get(id)

            if not employee:
                returned_code = 404

            data = request.form

            if 'first_name' in data:
                employee.first_name = data['first_name']

            if 'last_name' in data:
                employee.last_name = data['last_name']

            if 'job_title' in data:
                employee.job_title = data['job_title']

            if 'selectDepartment' in data:
                employee.department_id = data['selectDepartment']

            db.session.commit()
            db.session.close()
            
        except Exception as e:
            print("e: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()


        if returned_code != 200:
            abort(returned_code)
        else:
            return jsonify({
                'success':True,
                'message': 'Empleado actualizado correctamente'
                }), 200

    @app.route('/employees/<id>', methods=['DELETE'])
    def delete_employee(id):
        employee = Employee.query.get(id)

        if not employee:
            return jsonify({'success':False,'message': 'Empleado no encontrado'}), 404

        employee.is_active = False
        db.session.commit()
        db.session.close()

        return jsonify({'success':True,'message': 'Empleado eliminado correctamente'}), 200

    @app.route('/departments', methods=['GET'])
    def get_departments():
        try:
            search_query = request.args.get('query', None)
            if search_query:
                departments = Department.query.filter(
                    db.or_(Department.name.ilike('%{}%'.format(search_query)),
                            Department.short_name.ilike('%{}%'.format(search_query)))    
                ).all()

                return jsonify({'success': True, 'departments': [d.serialize() for d in departments], 'total': len(departments)}), 200

            departments = Department.query.order_by(Department.short_name).all()
            return jsonify({'success': True, 'departments': [d.serialize() for d in departments]}), 200


        except Exception as e:
            print("e: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Internal Server Error'}), 500
             
        
    @app.route('/departments', methods=['POST'])
    def create_department():
        error_code = 201
        list_errors = []
        try:
            body = request.json

            if 'name' not in body:
                list_errors.append('name is required')
            else:
                name = body.get('name')

            if 'short_name' not in body:
                list_errors.append('short_name is required')
            else:
                short_name = body.get('short_name')

            if len(list_errors) > 0:
                error_code = 400
            else:
                department = Department(name, short_name)
                db.session.add(department)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("error: ", e)
            print("sys.exc_info(): ", sys.exc_info())
            error_code = 500


        if error_code == 400:
            return jsonify({
                'success': False, 
                'message': 'Error creating department', 'errors': list_errors
            }), error_code
        elif error_code != 201:
            abort(error_code)
        else:
            return jsonify({
                'success': True, 
                 'id': department.id, 
                 'name':department.name, 
                 'short_name':department.short_name ,
                 'message': 'Department created successfully'
                 }), 201

    @app.route('/departments/<id>', methods=['PATCH'])
    def update_department(id):
        department = Department.query.get(id)

        if not department:
            return jsonify({'message': 'Departamento no encontrado'}), 404

        data = request.form

        if 'name' in data:
            department.name = data['name']
        if 'short_name' in data:
            department.short_name = data['short_name']
        db.session.commit()
        db.session.close()

        return jsonify({'success': True, 'message': 'Departamento actualizado exitosamente'})
    
    @app.route('/departments/<id>', methods=['DELETE'])
    def delete_department(id):
        department = Department.query.get(id)

        if not department:
            return jsonify({'message': 'Departamento no encontrado'}), 404

        db.session.delete(department)
        db.session.commit()
        db.session.close()

        return jsonify({'success': True,'message': 'Departamento eliminado exitosamente'})


    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({
            'success': False, 
            'message': 'Internal Server Error'
        }), 500
    
    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({
            'success': False,
            'message': 'Not Found'
        }), 404
    


    return app