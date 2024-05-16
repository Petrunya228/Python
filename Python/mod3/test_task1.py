import unittest
from freezegun import freeze_time
import datetime

from task1 import hello

class TestWeeekdays(unittest.TestCase):
    @freeze_time('2024-03-04')
    def test_week_monday(self):
        username=hello('art')
        self.assertEqual(username, "hello, art сейчас понедельник")

    @freeze_time('2024-03-05')
    def test_week_tuesday(self):
        username = hello('art')
        self.assertEqual(username, "hello, art сейчас вторник")

    @freeze_time('2024-03-06')
    def test_week_wednesday(self):
        username = hello('art')
        self.assertEqual(username, "hello, art сейчас среда")

    @freeze_time('2024-03-07')
    def test_week_thursday(self):
        username = hello('art')
        self.assertEqual(username, "hello, art сейчас четверг")

    @freeze_time('2024-03-08')
    def test_week_friday(self):
        username = hello('art')
        self.assertEqual(username, "hello, art сейчас пятница")

    @freeze_time('2024-03-09')
    def test_week_saturday(self):
        username = hello('art')
        self.assertEqual(username, "hello, art сейчас суббота")

    @freeze_time('2024-03-10')
    def test_week_sunday(self):
        username = hello('art')
        self.assertEqual(username, "hello, art сейчас воскресенье")
