import unittest
import subprocess


class TestExample4(unittest.TestCase):
    def test_output_430_1_40(self):
        # Test when the inputs are 430, 1, 40
        output = subprocess.check_output(['python3', 'example_4.py'], input='430\n1\n40\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes Helen needs to sleep: Enter the hour Helen goes to bed: Enter the minute Helen goes to bed: 8\n50\n')

    def test_output_300_23_0(self):
        # Test when the inputs are 300, 23, 0
        output = subprocess.check_output(['python3', 'example_4.py'], input='300\n23\n0\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes Helen needs to sleep: Enter the hour Helen goes to bed: Enter the minute Helen goes to bed: 4\n0\n')

    def test_output_1440_0_0(self):
        # Test when the inputs are 1440, 0, 0
        output = subprocess.check_output(['python3', 'example_4.py'], input='1440\n0\n0\n', text=True)
        self.assertEqual(output, 'Enter the number of minutes Helen needs to sleep: Enter the hour Helen goes to bed: Enter the minute Helen goes to bed: 0\n0\n')


if __name__ == '__main__':
    unittest.main()
