import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise7(CustomTestCase):

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
        Sums integers in '1 5 9 5 2 8' which should be 30
        """
        inputs = ['1 5 9 5 2 8']
        output = self.run_exercise(inputs)
        expected_output = "30"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Sums integers in '10 20 30' which should be 60
        """
        inputs = ['10 20 30']
        output = self.run_exercise(inputs)
        expected_output = "60"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Sums integers in '3 3 3 3 3' which should be 15
        """
        inputs = ['3 3 3 3 3']
        output = self.run_exercise(inputs)
        expected_output = "15"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Sums integers in '7 -2 3' which should be 8
        """
        inputs = ['7 -2 3']
        output = self.run_exercise(inputs)
        expected_output = "8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Sums integers in '0 0 0 0 0' which should be 0
        """
        inputs = ['0 0 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Sums integers in '100 200 300' which should be 600
        """
        inputs = ['100 200 300']
        output = self.run_exercise(inputs)
        expected_output = "600"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Sums integers in '-1 -2 -3 -4' which should be -10
        """
        inputs = ['-1 -2 -3 -4']
        output = self.run_exercise(inputs)
        expected_output = "-10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Sums integers in '50 25 75' which should be 150
        """
        inputs = ['50 25 75']
        output = self.run_exercise(inputs)
        expected_output = "150"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Sums integers in '1 1 1 1 1 1' which should be 6
        """
        inputs = ['1 1 1 1 1 1']
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Sums integers in '5 10 15 20' which should be 50
        """
        inputs = ['5 10 15 20']
        output = self.run_exercise(inputs)
        expected_output = "50"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
