import unittest
import subprocess
import os
import re
from .test_output_formatter import TestOutputFormatter


class CustomTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        # Set up common properties for all test methods
        self.exercise_file_name = self.determine_exercise_file_name()
        self.exercise_file_path = self.get_exercise_path(self.exercise_file_name)

    @classmethod
    def determine_exercise_file_name(cls):
        """Determines the exercise file name based on the test class name."""
        class_name = cls.__name__
        ex_number = class_name.split("TestExercise")[1]
        return f"exercise_{ex_number}.py"

    @staticmethod
    def get_exercise_path(exercise_file_name):
        """Constructs the absolute path to an exercise file."""
        current_dir = os.path.dirname(__file__)
        project_root = os.path.join(current_dir, "../../exercises")
        return os.path.normpath(os.path.join(project_root, exercise_file_name))
    
    @property
    def file_content(self):
        """
        Returns the content of the exercise file.
        """
        exercise_file_path = self.exercise_file_path
        with open(exercise_file_path, 'r') as file:
            content = file.read()
        return content

    def run_exercise(self, inputs):
        """Helper method to run the exercise script with the provided inputs and return its output."""
        input_value = '\n'.join(inputs) + '\n'
        return subprocess.check_output(['python3', self.exercise_file_path], input=input_value, text=True, universal_newlines=True)

    def assertInCustom(self, expected, actual, input_value, msg=None):
        try:
            self.assertIn(expected, actual)
        except AssertionError:
            custom_message = TestOutputFormatter.get_failure_details_in_table(input_value, expected.split('\n'), actual.split('\n'))
            if msg:
                custom_message += f"\nAdditional message: {msg}"
            raise AssertionError(custom_message)

    def assertUsesLoops(self):
        """
        Asserts that the solution uses a 'for' or 'while' loop.
        """
        try:
            self.assertTrue(self.check_for_loops())
        except AssertionError:
            loop_usage_message = TestOutputFormatter.generate_loop_usage_message()
            raise AssertionError(loop_usage_message)

    def assertUsesContinue(self):
        """
        Asserts that the solution uses the 'continue' statement.
        """
        try:
            self.assertTrue(self.check_for_continue())
        except AssertionError:
            continue_usage_message = TestOutputFormatter.generate_continue_usage_message()
            raise AssertionError(continue_usage_message)

    def assertNotUsesIf(self):
        """
        Asserts that the solution does not use the 'if' statement.
        """
        try:
            self.assertFalse(self.check_for_if())
        except AssertionError:
            if_usage_message = TestOutputFormatter.generate_if_usage_message()
            raise AssertionError(if_usage_message)

    def assertNotUsesList(self):
        """
        Asserts that the solution does not use lists.
        """
        try:
            self.assertFalse(self.check_for_list())
        except AssertionError:
            list_usage_message = TestOutputFormatter.generate_list_usage_message()
            raise AssertionError(list_usage_message)

    def assertNotUseStringSlice(self):
        """
        Asserts that the solution does not use string slicing.
        """
        try:
            self.assertFalse(self.check_for_string_slice())
        except AssertionError:
            string_slice_message = TestOutputFormatter.generate_string_slice_message()
            raise AssertionError(string_slice_message)

    def assertDivisionByZero(self):
        """
        Asserts that the solution does not divide by zero.
        """

        division_by_zero_message = TestOutputFormatter.generate_division_by_zero_message()
        raise AssertionError(division_by_zero_message)

    def assertNoProductSymbolUsage(self):
        """
        Asserts that the solution does not use the '*' symbol to calculate the product.
        """
        try:
            self.assertFalse(self.check_for_product_symbol())
        except AssertionError:
            message = TestOutputFormatter.generate_message("Product Symbol Usage Error", "The solution must not use the '*' symbol to calculate the product.")
            raise AssertionError(message)

    def assertAlmostEqualCustom(self, expected, actual, input_value, places=None, msg=None):
        """
        Asserts that two floating-point numbers are equal up to a certain number of decimal places.
        """
        try:
            # Remove non digit elements from the output
            actual = ''.join(list(filter(str.isdigit, actual)))
            self.assertAlmostEqual(float(expected), float(actual), places)
        except AssertionError:
            custom_message = TestOutputFormatter.get_failure_details_in_table(input_value, expected.split('\n'), actual.split('\n'))
            if msg:
                custom_message += f"\nAdditional message: {msg}"

    def assertNoUsesDictionary(self):
        """
        Asserts that the solution uses a dictionary.
        """
        try:
            self.assertFalse(self.check_for_dictionary())
        except AssertionError:
            dictionary_usage_message = TestOutputFormatter.generate_dictionary_usage_message()
            raise AssertionError(dictionary_usage_message)

    def assertNotUseSelfDefinedFunctions(self):
        """
        Asserts that the solution does not use self-defined functions.
        """
        try:
            self.assertFalse(self.check_for_self_defined_functions())
        except AssertionError:
            self_defined_functions_message = TestOutputFormatter.generate_self_defined_functions_message()
            raise AssertionError(self_defined_functions_message)

    def assertNotUsingProvidedSolution(self):
        """
        Asserts that the solution is not the provided solution.
        """
        try:
            self.assertFalse(self.check_for_provided_solution())
        except AssertionError:
            provided_solution_message = TestOutputFormatter.generate_provided_solution_message()
            raise AssertionError(provided_solution_message)

    def check_for_provided_solution(self):
        """
        Checks if the student's solution from exercises/exercise_{i}.py is 
        the same as the provided solution from solutions/solution_{i}.py.
        """
        exercise_number = self.exercise_file_name.split('_')[1].split('.')[0]
        solution_file_name = f"solution_{exercise_number}.py"
        solution_file_path = self.get_exercise_path(solution_file_name)
        with open(solution_file_path, 'r') as file:
            solution_content = file.read()
        return self.file_content == solution_content

    def check_for_self_defined_functions(self):
        """
        Checks if the solution file uses self-defined functions.
        """
        content = self.file_content
        return bool(re.search(r'def\s+\w+\(', content))

    def check_for_dictionary(self):
        """
        Checks if the solution file uses a dictionary by searching for dictionary literals
        and ensuring that these aren't confused with f-string usages.
        """
        content = self.file_content

        # Regex pattern to detect f-strings
        f_string_pattern = r"""
        f['"]         # f followed by a single or double quote
        .*?           # any characters, non-greedily
        \{.*?\}       # curly braces containing anything, used for formatting
        .*?           # any characters, non-greedily
        ['"]          # closing single or double quote
        """

        # Regex pattern to detect dictionary usage
        dictionary_pattern = r"""
        \{            # Opening brace
        \s*           # Optional whitespace inside the curly braces
        [^\s:{}]+     # At least one character that is not a colon, brace, or whitespace (key)
        \s*:\s*       # Colon with optional surrounding whitespace (key-value separator)
        [^\s{}]+      # At least one character that is not a brace or whitespace (value)
        \s*           # Optional whitespace before the closing brace
        \}            # Closing brace
        """

        return bool(re.search(dictionary_pattern, content)) and not bool(re.search(f_string_pattern, content))

    def check_for_loops(self):
        """
        Checks if the solution file uses 'for' or 'while' loops.
        """
        content = self.file_content
        return bool(re.search(r'\b(for|while)\b', content))

    def check_for_continue(self):
        """
        Checks if the solution file uses the 'continue' statement.
        """
        content = self.file_content
        return bool(re.search(r'\bcontinue\b', content))

    def check_for_if(self):
        """
        Checks if the solution file uses the 'if' statement.
        """
        content = self.file_content
        return bool(re.search(r'\bif\b', content))

    def check_for_list(self):
        """
        Checks if the solution file uses lists or list constructions.
        And split method
        """
        content = self.file_content
        return bool(re.search(r'\blist\b', content)) or bool(re.search(r'\.split\(', content)) or bool(re.search(r'\.append\(', content))

    def check_for_string_slice(self):
        """
        Checks if the solution file uses string slicing.
        """
        content = self.file_content
        return bool(re.search(r'\[.*:.*\]', content))

    def check_for_product_symbol(self):
        """
        Checks if the solution file uses the '*' symbol to calculate the product.
        """
        content = self.file_content
        return bool(re.search(r'\*', content))
