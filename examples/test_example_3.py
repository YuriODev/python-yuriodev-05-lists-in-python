import unittest
import subprocess


class TestExample3(unittest.TestCase):
    def test_output_450(self):
        # Test when the input is 450
        output = subprocess.check_output(['python3', 'example_3.py'], input='450\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes after midnight: 7\n30\n')

    def test_output_1240(self):
        # Test when the input is 1240
        output = subprocess.check_output(['python3', 'example_3.py'], input='1240\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes after midnight: 20\n40\n')

    def test_output_150(self):
        # Test when the input is 150
        output = subprocess.check_output(['python3', 'example_3.py'], input='150\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes after midnight: 2\n30\n')


if __name__ == '__main__':
    unittest.main()
