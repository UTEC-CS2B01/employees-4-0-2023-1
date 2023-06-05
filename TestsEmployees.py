import unittest
from app.models import Employee, Department
from app import create_app
config = {
    'DATABASE_URI': 'postgresql://postgres:1234@localhost:5432/christian',
}
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
        self.updated_department = {
        'name': 'Soport Technology',
        'short_name': 'ST'
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
    def test_get_departments(self):
        response = self.client.get('/departments')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue('departments' in data)
        if 'total' in data:
            self.assertTrue(data['total'] >= 0)

    def test_update_department(self):
        create_response = self.client.post('/departments', json=self.new_department)
        create_data = json.loads(create_response.data)
        department_id = create_data['id']
        update_response = self.client.patch(f'/departments/{department_id}', data=self.updated_department)
        update_data = json.loads(update_response.data)

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_data['success'], True)
        self.assertEqual(update_data['message'], 'Departamento actualizado exitosamente')
    def test_department_failed_update_404(self):
        sin_existencia_department_id = 1000
        response = self.client.delete(f'/departments/{sin_existencia_department_id}')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'Departamento no encontrado')

    def test_delete_department(self):
        create_response = self.client.post('/departments', json=self.new_department)
        create_data = json.loads(create_response.data)
        department_id = create_data['id']
        delete_response = self.client.delete(f'/departments/{department_id}')
        delete_data = json.loads(delete_response.data)

        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_data['success'], True)
        self.assertEqual(delete_data['message'], 'Departamento eliminado exitosamente')
    def test_delete_department_failed_404(self):
        sin_existencia_department_id = 200
        response = self.client.delete(f'/departments/{sin_existencia_department_id}')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['message'], 'Departamento no encontrado')
    
    
class TestCreateEmployee(unittest.TestCase):
    def setUp(self):
        database_qa = config['DATABASE_URI']
        self.app = create_app({ 'database_qa': database_qa })
        self.client = self.app.test_client()
        self.new_employee={
                'first_name': 'Christian',
                'last_name': 'Frisancho',
                'job_title': 'Medico',
        }
        self.new_failed_employee = {
            'first_name': 'Christian'
        }

    def test_create_employee_success(self):

        response = self.client.post('/employees', json=self.new_employee)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['id'])


    def tearDown(self):
        pass
