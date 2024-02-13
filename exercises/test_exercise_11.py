import unittest
import subprocess
import os

# Define the full path to the exercise script
exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_11.py")


class TestBillDenominations(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_example_1(self):
        """Test the provided example 1."""
        output = self.run_exercise("534\n")
        self.assertEqual(output, "1 (500), 0 (100), 3 (10), 0 (5), 4 (1)\n")

    def test_example_2(self):
        """Test the provided example 2."""
        output = self.run_exercise("1245\n")
        self.assertEqual(output, "2 (500), 2 (100), 4 (10), 1 (5), 0 (1)\n")

    def test_example_3(self):
        """Test the provided example 3."""
        output = self.run_exercise("12\n")
        self.assertEqual(output, "0 (500), 0 (100), 1 (10), 0 (5), 2 (1)\n")

    def test_example_4(self):
        """Test the provided example 4."""
        output = self.run_exercise("786\n")
        self.assertEqual(output, "1 (500), 2 (100), 8 (10), 1 (5), 1 (1)\n")

    def test_example_5(self):
        """Test the provided example 5."""
        output = self.run_exercise("377\n")
        self.assertEqual(output, "0 (500), 3 (100), 7 (10), 1 (5), 2 (1)\n")




if __name__ == '__main__':
    unittest.main()