import unittest
import subprocess


class TestExample10(unittest.TestCase):
    def test_output_184(self):
        # Test when the input is 184
        output = subprocess.check_output(['python3', 'example_10.py'], input='184\n', text=True)
        self.assertEqual(output, 'Enter a three-digit number: 481\n')

    def test_output_123(self):
        # Test when the input is 123
        output = subprocess.check_output(['python3', 'example_10.py'], input='123\n', text=True)
        self.assertEqual(output, 'Enter a three-digit number: 321\n')

    def test_output_567(self):
        # Test when the input is 567
        output = subprocess.check_output(['python3', 'example_10.py'], input='567\n', text=True)
        self.assertEqual(output, 'Enter a three-digit number: 765\n')


if __name__ == '__main__':
    unittest.main()
