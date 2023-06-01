import unittest
from app.models import Employee, Department
from app import create_app
from config.test import config
import json

class TestsEmployees(unittest.TestCase):

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
