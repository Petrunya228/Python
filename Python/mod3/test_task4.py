import unittest
import datetime

from task4 import Person

class testPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('art', 2004, '123 main street')

    def test_age(self):
        self.assertEqual(self.person.get_age(), datetime.datetime.now().year - 2004)

    def test_name(self):
        self.assertEqual(self.person.get_name(), 'art')

    def test_set_name(self):
        self.person.set_name('bob')
        self.assertEqual(self.person.get_name(), 'bob')

    def test_set_adress(self):
        self.person.set_address('current street')
        self.assertEqual(self.person.get_address(), 'current street')

    def test_get_adress(self):
        self.assertEqual(self.person.get_address(), '123 main street')

    def test_home(self):
        self.assertFalse(self.person.is_homeless())
