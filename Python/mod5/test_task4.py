import unittest
import sys
from task4 import Redirect

class TestRedirect(unittest.TestCase):
    def test_stdout_redirected(self):
        stdout_file = open('test_stdout.txt', 'w')
        stderr_file = open('test_stderr.txt', 'w')

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Тест перенаправления stdout')
            self.assertEqual(sys.stdout, stdout_file)

    def test_stderr_redirected(self):
        stdout_file = open('test_stdout.txt', 'w')
        stderr_file = open('test_stderr.txt', 'w')

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            try:
                raise Exception('Тест перенаправления stderr')
            except Exception:
                pass
            self.assertEqual(sys.stderr, stderr_file)

if __name__ == '__main__':
    with open('test_results.txt', 'a') as test_file_stream:
        runner = unittest.TextTestRunner(stream=test_file_stream)
        unittest.main(testRunner=runner)
