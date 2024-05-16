import json
import unittest
from task3 import app


class testFinance(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.app = app.test_client()

    def test_add_expense(self):
        response=self.app.get('/add/20230103/50')
        self.assertEqual(response.status_code, 200) # проверяем ответ от сервера (200- все норм)
        self.assertIn(b'spending - 50', response.data)

    def test_add_bad_expense(self):
        response=self.app.get('/add/202301/50')
        self.assertRaises(AssertionError) # проверяем ответ от сервера (200- все норм)
        self.assertIn(b'spending - 50', response.data)

    def test_calculate_year(self):
        response = self.app.get('/calculate/2022')
        self.assertEqual(response.status_code, 200)# аналог assertRaises. также кинет ошибку
        self.assertIn(b'spending - 300', response.data)

    def test_calculate_month(self):
        response=self.app.get('/calculate/2024/05')
        self.assertEqual(response.status_code, 200)# аналог assertRaises. также кинет ошибку
        self.assertIn(b'spending - 320', response.data)
