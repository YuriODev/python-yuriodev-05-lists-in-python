import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise13(CustomTestCase):

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
        Calculates the arithmetic mean of '3 5 1 8 4' which should be 4.20
        """
        inputs = ['3 5 1 8 4']
        output = self.run_exercise(inputs)
        expected_output = "4.20"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Calculates the arithmetic mean of '10 20 30 40 50' which should be 30.00
        """
        inputs = ['10 20 30 40 50']
        output = self.run_exercise(inputs)
        expected_output = "30.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Calculates the arithmetic mean of '2 4 6 8' which should be 5.00
        """
        inputs = ['2 4 6 8']
        output = self.run_exercise(inputs)
        expected_output = "5.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Calculates the arithmetic mean of '1 1 1 1 1' which should be 1.00
        """
        inputs = ['1 1 1 1 1']
        output = self.run_exercise(inputs)
        expected_output = "1.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Calculates the arithmetic mean of '5 5 5 5' which should be 5.00
        """
        inputs = ['5 5 5 5']
        output = self.run_exercise(inputs)
        expected_output = "5.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Calculates the arithmetic mean of '1 2 3 4 5' which should be 3.00
        """
        inputs = ['1 2 3 4 5']
        output = self.run_exercise(inputs)
        expected_output = "3.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Calculates the arithmetic mean of '0 0 0 0 0' which should be 0.00
        """
        inputs = ['0 0 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "0.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Calculates the arithmetic mean of '4 6 8 10 12' which should be 8.00
        """
        inputs = ['4 6 8 10 12']
        output = self.run_exercise(inputs)
        expected_output = "8.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Calculates the arithmetic mean of '7 14 21 28' which should be 17.50
        """
        inputs = ['7 14 21 28']
        output = self.run_exercise(inputs)
        expected_output = "17.50"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Calculates the arithmetic mean of '100 200 300' which should be 200.00
        """
        inputs = ['100 200 300']
        output = self.run_exercise(inputs)
        expected_output = "200.00"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
