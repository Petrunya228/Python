import unittest

from task2 import decrypt

class testDecrypt(unittest.TestCase):
    def test_decrypt_1(self):
        test=decrypt('абра-кадабра.')
        self.assertEqual(test, 'абра-кадабра')

    def test_decrypt_2(self):
        test=decrypt('абраа..-кадабра')
        self.assertEqual(test, 'абра-кадабра')

    def test_decrypt_3(self):
        test=decrypt('абраа..-.кадабра')
        self.assertEqual(test, 'абра-кадабра')

    def test_decrypt_4(self):
        test=decrypt('абра--..кадабра')
        self.assertEqual(test, 'абра-кадабра')

    def test_decrypt_5(self):
        test=decrypt('абрау...-кадабра')
        self.assertEqual(test, 'абра-кадабра')

    def test_decrypt_6(self):
        test=decrypt('абра........')
        self.assertEqual(test, '')

    def test_decrypt_7(self):
        test=decrypt('абр......a.')
        self.assertEqual(test, 'a')

    def test_decrypt_8(self):
        test=decrypt('1..2.3')
        self.assertEqual(test, '23')

    def test_decrypt_9(self):
        test=decrypt('.')
        self.assertEqual(test, '')

    def test_decrypt_10(self):
        test=decrypt('1.......................')
        self.assertEqual(test, '')
