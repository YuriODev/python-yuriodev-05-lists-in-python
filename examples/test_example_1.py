import unittest
import subprocess


class TestExample1(unittest.TestCase):
    def test_output_1981(self):
        # Test when the input is 1981
        output = subprocess.check_output(['python3', 'example_1.py'], input='1981\n', text=True)
        self.assertIn('The tens place digit of 1981 is 8', output)

    def test_output_158(self):
        # Test when the input is 158
        output = subprocess.check_output(['python3', 'example_1.py'], input='158\n', text=True)
        self.assertIn('The tens place digit of 158 is 5', output)

    def test_output_5(self):
        # Test when the input is 5
        output = subprocess.check_output(['python3', 'example_1.py'], input='5\n', text=True)
        self.assertIn('The tens place digit of 5 is 0', output)


if __name__ == '__main__':
    unittest.main()
