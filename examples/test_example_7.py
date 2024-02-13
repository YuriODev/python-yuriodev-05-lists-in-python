import unittest
import subprocess


class TestExample7(unittest.TestCase):
    def test_output_456712_2(self):
        # Test when the inputs are 456712 and 2
        output = subprocess.check_output(['python3', 'example_7.py'], input='456712\n2\n', text=True)
        self.assertEqual(output, 'Enter the integer: Enter the number of digits to cut off: 4567\n')

    def test_output_123456_3(self):
        # Test when the inputs are 123456 and 3
        output = subprocess.check_output(['python3', 'example_7.py'], input='123456\n3\n', text=True)
        self.assertEqual(output, 'Enter the integer: Enter the number of digits to cut off: 123\n')

    def test_output_123456_6(self):
        # Test when the inputs are 123456 and 6
        output = subprocess.check_output(['python3', 'example_7.py'], input='123456\n6\n', text=True)
        self.assertEqual(output, 'Enter the integer: Enter the number of digits to cut off: 0\n')


if __name__ == '__main__':
    unittest.main()
