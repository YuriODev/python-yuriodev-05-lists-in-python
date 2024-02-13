import unittest
import subprocess
import os

# Define the full path to the exercise script
exercise_file_path = os.path.join(os.path.dirname(__file__), "exercise_1.py")


class TestExample1(unittest.TestCase):
    def run_exercise(self, input_value):
        """Helper method to run the exercise script with the provided input and return its output."""
        return subprocess.check_output(['python3', exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def test_example_1(self):
        """Test the provided example 1."""
        output = self.run_exercise("12345\n")
        self.assertIn("96\n", output)

    def test_example_2(self):
        """Test the provided example 2."""
        output = self.run_exercise("44444\n")
        self.assertIn("128\n", output)

    def test_example_3(self):
        """Test the provided example 3."""
        output = self.run_exercise("11111\n")
        self.assertIn("32\n", output)

    def test_example_4(self):
        """Test the provided example 4."""
        output = self.run_exercise("12346\n")
        self.assertIn("106\n", output)


if __name__ == '__main__':
    unittest.main()