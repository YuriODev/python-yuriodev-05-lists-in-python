import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise32(CustomTestCase):

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
        Longest line among 5 inputs
        """
        inputs = ['5', 'Thames', 'Amazon', 'Nile', 'Yangtze', 'Dnieper']
        output = self.run_exercise(inputs)
        expected_output = "4\n5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Longest line among 3 inputs
        """
        inputs = ['3', 'short', 'medium length', 'longest line']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Longest line among 4 inputs
        """
        inputs = ['4', 'alpha', 'beta', 'gamma', 'delta']
        output = self.run_exercise(inputs)
        expected_output = "1\n3\n4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Longest line among 2 inputs
        """
        inputs = ['2', 'quick', 'quickest']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Single line input
        """
        inputs = ['1', 'onlyone']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Empty lines
        """
        inputs = ['3', '', '', '']
        output = self.run_exercise(inputs)
        expected_output = "1\n2\n3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Multiple longest lines of different lengths
        """
        inputs = ['4', 'short', 'longer line', 'longest line of all', 'longest line of all']
        output = self.run_exercise(inputs)
        expected_output = "3\n4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        First line is the longest
        """
        inputs = ['3', 'this is the longest line', 'short', 'medium']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Last line is the longest
        """
        inputs = ['3', 'short', 'medium', 'this is the longest line']
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Multiple lines with the same length
        """
        inputs = ['5', 'line one', 'line two', 'line three', 'line four', 'line five']
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
