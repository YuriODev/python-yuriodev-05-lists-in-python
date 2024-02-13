import unittest
import subprocess


class TestExample2(unittest.TestCase):
    def test_output_153(self):
        # Test when the input is 153
        output = subprocess.check_output(['python3', 'example_2.py'], input='153\n', text=True)
        self.assertIn('The sum of the digits of 153 is 9', output)

    def test_output_123(self):
        # Test when the input is 123
        output = subprocess.check_output(['python3', 'example_2.py'], input='123\n', text=True)
        self.assertIn('The sum of the digits of 123 is 6', output)

    def test_output_565(self):
        # Test when the input is 565
        output = subprocess.check_output(['python3', 'example_2.py'], input='565\n', text=True)
        self.assertIn('The sum of the digits of 565 is 16', output)


if __name__ == '__main__':
    unittest.main()
