import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise28(CustomTestCase):

    def test_dict_usage(self):
        """
        The program should not use dictionaries to solve the exercise.
        """

        self.assertNoUsesDictionary()

    def test_function_usage(self):
        """
        The program should not use functions to solve the exercise.
        """

        self.assertNotUseSelfDefinedFunctions()

    def provided_soltuion_usage(self):
        """
        The program should not use the provided solution to solve 
        the exercise.
        """

        self.assertNotUsingProvidedSolution()

    def test_case_1(self):
        """
        Extract head and tail with multiple elements
        """
        inputs = ['2 10 15 9 3 6 7 11']
        output = self.run_exercise(inputs)
        expected_output = "2\n10 15 9 3 6 7 11"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Extract head and tail with consecutive numbers
        """
        inputs = ['5 6 7 8 9']
        output = self.run_exercise(inputs)
        expected_output = "5\n6 7 8 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Extract head and tail with odd numbers
        """
        inputs = ['1 3 5 7 9']
        output = self.run_exercise(inputs)
        expected_output = "1\n3 5 7 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Extract head and tail with even numbers
        """
        inputs = ['4 8 12 16']
        output = self.run_exercise(inputs)
        expected_output = "4\n8 12 16"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Extract head and tail with a single element
        """
        inputs = ['42']
        output = self.run_exercise(inputs)
        expected_output = "42"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Extract head and tail with negative numbers
        """
        inputs = ['-1 -2 -3 -4']
        output = self.run_exercise(inputs)
        expected_output = "-1\n-2 -3 -4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Extract head and tail with zero included
        """
        inputs = ['0 1 2 3 4']
        output = self.run_exercise(inputs)
        expected_output = "0\n1 2 3 4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Extract head and tail with large numbers
        """
        inputs = ['1000000 2000000 3000000']
        output = self.run_exercise(inputs)
        expected_output = "1000000\n2000000 3000000"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Extract head and tail with mixed positive and negative numbers
        """
        inputs = ['-5 10 -15 20']
        output = self.run_exercise(inputs)
        expected_output = "-5\n10 -15 20"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Extract head and tail with random numbers
        """
        inputs = ['23 56 78 99 102']
        output = self.run_exercise(inputs)
        expected_output = "23\n56 78 99 102"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
