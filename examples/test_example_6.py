import unittest
import subprocess


class TestExample6(unittest.TestCase):
    def test_output_150(self):
        # Test when the input is 150
        output = subprocess.check_output(['python3', 'example_6.py'], input='150\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes that have passed since midnight: 2, 30\n')

    def test_output_25(self):
        # Test when the input is 25
        output = subprocess.check_output(['python3', 'example_6.py'], input='25\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes that have passed since midnight: 0, 25\n')

    def test_output_440(self):
        # Test when the input is 440
        output = subprocess.check_output(['python3', 'example_6.py'], input='440\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes that have passed since midnight: 7, 20\n')


if __name__ == '__main__':
    unittest.main()
