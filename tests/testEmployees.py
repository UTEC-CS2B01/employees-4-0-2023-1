import unittest

from flask import Flask
from flask_testing import TestCase
from __init__ import test_app


class EmployeesTest(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_create_employee(self):
        data = {
            'first_name': 'Christian',
            'last_name': 'Frisancho',
            'job_title': 'Chef',
            'selectDepartment': 2
        }

        response = self.client.post('/employees', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json)
        self.assertIn('first_name', response.json)
        self.assertIn('last_name', response.json)
        self.assertIn('job_title', response.json)
        self.assertIn('department_id', response.json)
        self.assertEqual(response.json['message'], 'Empleado creado correctamente')

    def test_get_employees(self):
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertIn('employees', response.json)
        self.assertIsInstance(response.json['employees'], list)

    def test_update_employee(self):
        data = {
            'first_name': 'Maxim',
            'last_name': 'Mayorga',
            'job_title': 'Medico',
            'selectDepartment': 5
        }

        response = self.client.patch('/employees/<id>', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json)
        self.assertIn('first_name', response.json)
        self.assertIn('last_name', response.json)
        self.assertIn('job_title', response.json)
        self.assertIn('department_id', response.json)
        self.assertEqual(response.json['message'], 'Empleado cambiado correctamente')

    def test_delete_employee(self):
        response = self.client.delete('/employees/<id>')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Empleado eliminado correctamente')


if __name__ == '__main__':
    unittest.main()
