import unittest
from app.models import Employee, Department
from app import create_app
from config.test import config
import json

class TestsDepartments(unittest.TestCase):

    def setUp(self):
        database_qa = config['DATABASE_URI']
        self.app = create_app({ 'database_qa': database_qa })
        self.client = self.app.test_client()

        self.new_department = {
            'name': 'Information Technology',
            'short_name': 'TI'
        }

        self.new_failed_department = {
            'name': 'Information Technology'
        }


    def test_create_department_success(self):
        response = self.client.post('/departments', json=self.new_department)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['id'])

    def test_create_department_failed_400(self):
        response = self.client.post('/departments', json=self.new_failed_department)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Error creating department')
        self.assertTrue(data['errors'])

    def test_create_department_failed_500(self):
        response = self.client.post('/departments', json={'name': None, 'short_name': None})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
    

    def tearDown(self):
        pass


class TestEmployees(unittest.TestCase):

    def setUp(self):
        database_qa = config['DATABASE_URI']
        self.app = create_app({ 'database_qa': database_qa })
        self.client = self.app.test_client()

        self.new_employee = {
            'first_name': 'John',
            'last_name': 'Doe',
            'job_title': 'Software Engineer',
            'selectDepartment': '067551db-003d-49a2-a3c9-b746b7b0aea6'
        }

    def test_create_employee_success(self):
        response = self.client.post('/employees', json=self.new_employee)
        data = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['id'])
        self.assertEqual(data['message'], 'Employee created successfully')

    def test_create_employee_missing_fields(self):
        response = self.client.post('/employees', json={})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Error creating employee')
        self.assertTrue(data['errors'])
        self.assertIn('first_name is required', data['errors'])
        self.assertIn('last_name is required', data['errors'])
        self.assertIn('job_title is required', data['errors'])
        self.assertIn('selectDepartment is required', data['errors'])

    def test_create_employee_internal_server_error(self):
        response = self.client.post('/employees', json={
            'first_name': None,
            'last_name': None,
            'job_title': None,
            'selectDepartment': None
        })
        data = response.get_json()

        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Internal Server Error')

    def test_get_employees(self):
        response = self.client.get('/employees')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['employees'])
        self.assertTrue(data['total'])

    def test_update_employee(self):
        # 1. Crear un empleado
        create_response = self.client.post('/employees', json=self.new_employee)
        create_data = create_response.get_json()

        # 2. Actualizar los datos del empleado
        employee_id = create_data['id']
        update_data = {
            'first_name': 'John Updated',
            'last_name': 'Doe Updated',
            'job_title': 'Senior Software Engineer',
        }
        update_response = self.client.patch(f'/employees/{employee_id}', json=update_data)
        update_data = update_response.get_json()

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_data['success'], True)
        self.assertEqual(update_data['message'], 'Empleado actualizado correctamente')

    def test_delete_employee(self):
        # 1. Crear un empleado
        create_response = self.client.post('/employees', json=self.new_employee)
        create_data = create_response.get_json()

        # 2. Eliminar el empleado
        employee_id = create_data['id']
        delete_response = self.client.delete(f'/employees/{employee_id}')
        delete_data = delete_response.get_json()

        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_data['success'], True)
        self.assertEqual(delete_data['message'], 'Empleado eliminado correctamente')

    def tearDown(self):
        pass
