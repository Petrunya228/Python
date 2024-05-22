import unittest

from task3 import BlockErrors

class TestBlock(unittest.TestCase):
    def test_ignore_error(self):
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors(TypeError):
                a=1/0

    def test_propagate_error(self):
        with self.assertRaises(TypeError):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'

    def test_inner_ignore_outer_propagate(self):
        with self.assertRaises(TypeError):
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                print('Внутренний блок: выполнено без ошибок')
            print('Внешний блок: выполнено без ошибок')

if __name__ == '__main__':
    unittest.main()