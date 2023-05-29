import unittest
from models import db, Department

class TestDepartments(unittest.TestCase):
    def setUp(self):
        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_create_department(self):
        # Crea nuevo departamento
        new_department = Department(name='Marketing', short_name='MKT')
        self.db.session.add(new_department)
        self.db.session.commit()

        departments = Department.query.all()
        self.assertEqual(len(departments), 1)
        self.assertEqual(departments[0].name, 'Marketing')
        self.assertEqual(departments[0].short_name, 'MKT')

if __name__ == "__main__":
    unittest.main()
