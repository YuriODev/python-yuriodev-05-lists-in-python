import unittest
import subprocess


class TestExample9(unittest.TestCase):
    def test_output_100(self):
        # Test when the input is 100
        output = subprocess.check_output(['python3', 'example_9.py'], input='100\n', text=True)
        self.assertEqual(output, 'Enter the number of natural numbers to sum: 5050\n')

    def test_output_15(self):
        # Test when the input is 15
        output = subprocess.check_output(['python3', 'example_9.py'], input='15\n', text=True)
        self.assertEqual(output, 'Enter the number of natural numbers to sum: 120\n')

    def test_output_99(self):
        # Test when the input is 99
        output = subprocess.check_output(['python3', 'example_9.py'], input='99\n', text=True)
        self.assertEqual(output, 'Enter the number of natural numbers to sum: 4950\n')


if __name__ == '__main__':
    unittest.main()
