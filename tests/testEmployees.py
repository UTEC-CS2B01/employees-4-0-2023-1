import unittest
from app.models import Employee
from datetime import datetime
import uuid

class TestEmployeeModel(unittest.TestCase):

    def setUp(self):
        self.id = str(uuid.uuid4())
        self.first_name = "Jose"
        self.last_name = "Suarez"
        self.job_title = "Software Engineer"
        self.department_id = str(uuid.uuid4()) 
        self.employee = Employee(self.first_name, self.last_name, self.job_title, self.department_id)

    def test_employee_creation(self):
        self.assertEqual(self.employee.first_name, self.first_name)
        self.assertEqual(self.employee.last_name, self.last_name)
        self.assertEqual(self.employee.job_title, self.job_title)
        self.assertEqual(self.employee.department_id, self.department_id)
        self.assertEqual(self.employee.is_active, True)

    def test_employee_repr(self):
        self.assertEqual(self.employee.__repr__(), '<Employee %r %r>' % (self.first_name, self.last_name))

    def test_employee_serialization(self):
        created_at_str = datetime.strftime(self.employee.created_at, "%B %d of %Y at %I:%M %p")
        self.assertDictEqual(self.employee.serialize(), 
                             {'id': self.employee.id, 
                              'first_name': self.first_name,
                              'last_name': self.last_name,
                              'job_title': self.job_title,
                              'created_at': created_at_str,
                              'image_path': self.employee.image_path
                             })

if __name__ == '__main__':
    unittest.main()
