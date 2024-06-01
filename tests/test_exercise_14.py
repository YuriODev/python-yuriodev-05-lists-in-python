import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise14(CustomTestCase):

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
        Calculates the distance between points (2, 3) and (-7, 4) which should be 9.06
        """
        inputs = ['2 3 -7 4']
        output = self.run_exercise(inputs)
        expected_output = "9.06"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Calculates the distance between points (0, 0) and (3, 4) which should be 5.00
        """
        inputs = ['0 0 3 4']
        output = self.run_exercise(inputs)
        expected_output = "5.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Calculates the distance between points (1, 1) and (4, 5) which should be 5.00
        """
        inputs = ['1 1 4 5']
        output = self.run_exercise(inputs)
        expected_output = "5.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Calculates the distance between points (-1, -1) and (1, 1) which should be 2.83
        """
        inputs = ['-1 -1 1 1']
        output = self.run_exercise(inputs)
        expected_output = "2.83"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Calculates the distance between points (1, 2) and (4, 6) which should be 5.00
        """
        inputs = ['1 2 4 6']
        output = self.run_exercise(inputs)
        expected_output = "5.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Calculates the distance between points (-5, -5) and (5, 5) which should be 14.14
        """
        inputs = ['-5 -5 5 5']
        output = self.run_exercise(inputs)
        expected_output = "14.14"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Calculates the distance between points (0, 0) and (0, 0) which should be 0.00
        """
        inputs = ['0 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "0.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Calculates the distance between points (3, 4) and (6, 8) which should be 5.00
        """
        inputs = ['3 4 6 8']
        output = self.run_exercise(inputs)
        expected_output = "5.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Calculates the distance between points (7, 8) and (10, 11) which should be 4.24
        """
        inputs = ['7 8 10 11']
        output = self.run_exercise(inputs)
        expected_output = "4.24"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Calculates the distance between points (-2, -3) and (3, 4) which should be 9.22
        """
        inputs = ['-2 -3 3 4']
        output = self.run_exercise(inputs)
        expected_output = "8.60"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
