import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise35(CustomTestCase):

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
        Compress list by moving non-zero elements to the left
        """
        inputs = ['6 0 3 0 5 0 0 4']
        output = self.run_exercise(inputs)
        expected_output = "6 3 5 4 0 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Compress list with non-zero elements at the start
        """
        inputs = ['1 2 0 0 3 4 0 5']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Compress list with zeros at the start
        """
        inputs = ['0 0 1 2 3 0 4 5']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Compress list with zeros in the middle
        """
        inputs = ['5 0 0 0 0 1 2 3']
        output = self.run_exercise(inputs)
        expected_output = "5 1 2 3 0 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Compress list with no zeros
        """
        inputs = ['1 2 3 4 5 6']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Compress list with all zeros
        """
        inputs = ['0 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "0 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Compress list with alternating zeros
        """
        inputs = ['1 0 2 0 3 0 4 0']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 0 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Compress list with single element
        """
        inputs = ['5']
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Compress list with single zero
        """
        inputs = ['0']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Compress list with large numbers
        """
        inputs = ['100 0 200 0 300 0 400 0']
        output = self.run_exercise(inputs)
        expected_output = "100 200 300 400 0 0 0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
