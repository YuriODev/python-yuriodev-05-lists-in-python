import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise12(CustomTestCase):

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
        Converts '1 7 9 4' to 1794
        """
        inputs = ['1 7 9 4']
        output = self.run_exercise(inputs)
        expected_output = "1794"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Converts '3 4 5' to 345
        """
        inputs = ['3 4 5']
        output = self.run_exercise(inputs)
        expected_output = "345"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Converts '8 0 2 5' to 8025
        """
        inputs = ['8 0 2 5']
        output = self.run_exercise(inputs)
        expected_output = "8025"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Converts '6 1 4' to 614
        """
        inputs = ['6 1 4']
        output = self.run_exercise(inputs)
        expected_output = "614"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Converts '2 0 2 1' to 2021
        """
        inputs = ['2 0 2 1']
        output = self.run_exercise(inputs)
        expected_output = "2021"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Converts '9 8 7 6' to 9876
        """
        inputs = ['9 8 7 6']
        output = self.run_exercise(inputs)
        expected_output = "9876"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Converts '4 4 4 4' to 4444
        """
        inputs = ['4 4 4 4']
        output = self.run_exercise(inputs)
        expected_output = "4444"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Converts '0 1 2 3' to 123
        """
        inputs = ['0 1 2 3']
        output = self.run_exercise(inputs)
        expected_output = "123"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Converts '1 0 0 0' to 1000
        """
        inputs = ['1 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "1000"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Converts '5 5 5 5' to 5555
        """
        inputs = ['5 5 5 5']
        output = self.run_exercise(inputs)
        expected_output = "5555"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
