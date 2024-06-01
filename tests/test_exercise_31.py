import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise31(CustomTestCase):

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
        Sum of neighbors for a list of 5 numbers
        """
        inputs = ['1 3 5 6 10']
        output = self.run_exercise(inputs)
        expected_output = "13 6 9 15 7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Sum of neighbors for a single number
        """
        inputs = ['5']
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Sum of neighbors for a list of 5 even numbers
        """
        inputs = ['2 4 6 8 10']
        output = self.run_exercise(inputs)
        expected_output = "14 8 12 16 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Sum of neighbors for a list of 4 consecutive numbers
        """
        inputs = ['7 8 9 10']
        output = self.run_exercise(inputs)
        expected_output = "18 16 18 16"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Sum of neighbors for a list with negative numbers
        """
        inputs = ['-1 -2 -3 -4']
        output = self.run_exercise(inputs)
        expected_output = "-6 -4 -6 -4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Sum of neighbors for a list with mix of positive and negative numbers
        """
        inputs = ['3 -3 5 -5']
        output = self.run_exercise(inputs)
        expected_output = "-8 8 -8 8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Sum of neighbors for a list of repeating numbers
        """
        inputs = ['2 2 2 2']
        output = self.run_exercise(inputs)
        expected_output = "4 4 4 4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Sum of neighbors for a list with zeroes
        """
        inputs = ['0 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "0 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Sum of neighbors for a list with mixed values
        """
        inputs = ['1 0 -1 0 1']
        output = self.run_exercise(inputs)
        expected_output = "1 0 0 0 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Sum of neighbors for a large list
        """
        inputs = ['1 2 3 4 5 6 7 8 9 10']
        output = self.run_exercise(inputs)
        expected_output = "12 4 6 8 10 12 14 16 18 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
