import unittest
import subprocess


class TestExample5(unittest.TestCase):
    def test_output_6785(self):
        # Test when the input is 6785
        output = subprocess.check_output(['python3', 'example_5.py'], input='6785\n', text=True)
        self.assertEqual(output, 'Enter the number of seconds: 0 day(s), 1 hour(s), 53 minute(s), 5 second(s)\n')

    def test_output_456789(self):
        # Test when the input is 456789
        output = subprocess.check_output(['python3', 'example_5.py'], input='456789\n', text=True)
        self.assertEqual(output, 'Enter the number of seconds: 5 day(s), 6 hour(s), 53 minute(s), 9 second(s)\n')

    def test_output_86401(self):
        # Test when the input is 86401
        output = subprocess.check_output(['python3', 'example_5.py'], input='86401\n', text=True)
        self.assertEqual(output, 'Enter the number of seconds: 1 day(s), 0 hour(s), 0 minute(s), 1 second(s)\n')


if __name__ == '__main__':
    unittest.main()
