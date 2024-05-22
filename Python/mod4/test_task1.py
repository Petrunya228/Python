import unittest
from task1 import app

class testInf(unittest.TestCase):
    data = {
        'email': 'test@example.com',
        'phone': 8800555355,
        'name': 'Дядя Тёма',
        'address': 'main Street',
        'index': 18745
    }
    def setUp(self):
        app.config["WTF_CSRF_ENABLED"] = False
        self.app=app.test_client()

    def test_all(self):
        response=self.app.post('/registration', data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_email(self):
        data = {
            'email': 'урраааа',
            'phone': 8800555355,
            'name': 'Дядя Тёма',
            'address': 'main Street',
            'index': 18745
        }
        response = self.app.post('/registration', data=data)
        self.assertEqual(response.status_code,400)

    def test_phone(self):
        data = {
            'email': 'test@example.com',
            'phone': 87,
            'name': 'Дядя Тёма',
            'address': 'main Street',
            'index': 18745
        }
        response = self.app.post('/registration', data=data)
        self.assertEqual(response.status_code, 400)

    def test_empty(self):
        data = {
            'email': 'test@example.com',
            'phone': 8905802082,
            'name': '',
            'address': 'main Street',
            'index': 18745
        }
        response = self.app.post('/registration', data=data)
        self.assertEqual(response.status_code, 400)


if __name__ == 'main':
    unittest.main()
