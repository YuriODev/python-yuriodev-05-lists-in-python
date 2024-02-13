import unittest
import subprocess


class TestExample8(unittest.TestCase):
    def test_output_10_15_2(self):
        # Test when the inputs are 10, 15, and 2
        output = subprocess.check_output(['python3', 'example_8.py'], input='10\n15\n2\n', text=True)
        self.assertEqual(output, 'Enter the cost of a book in pounds: Enter the cost of a book in pennies: Enter the number of books: 20\n30\n')

    def test_output_5_50_4(self):
        # Test when the inputs are 5, 50, and 4
        output = subprocess.check_output(['python3', 'example_8.py'], input='5\n50\n4\n', text=True)
        self.assertEqual(output, 'Enter the cost of a book in pounds: Enter the cost of a book in pennies: Enter the number of books: 22\n0\n')

    def test_output_1_99_1(self):
        # Test when the inputs are 1, 99, and 1
        output = subprocess.check_output(['python3', 'example_8.py'], input='1\n99\n1\n', text=True)
        self.assertEqual(output, 'Enter the cost of a book in pounds: Enter the cost of a book in pennies: Enter the number of books: 1\n99\n')


if __name__ == '__main__':
    unittest.main()
