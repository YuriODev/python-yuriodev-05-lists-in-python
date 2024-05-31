import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise8(CustomTestCase):

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
        Separates integer and fractional parts of '12.567' which should be '12 567'
        """
        inputs = ['12.567']
        output = self.run_exercise(inputs)
        expected_output = "12 567"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Separates integer and fractional parts of '0.75' which should be '0 75'
        """
        inputs = ['0.75']
        output = self.run_exercise(inputs)
        expected_output = "0 75"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Separates integer and fractional parts of '45.1234' which should be '45 1234'
        """
        inputs = ['45.1234']
        output = self.run_exercise(inputs)
        expected_output = "45 1234"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Separates integer and fractional parts of '100.001' which should be '100 001'
        """
        inputs = ['100.001']
        output = self.run_exercise(inputs)
        expected_output = "100 001"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Separates integer and fractional parts of '0.0' which should be '0 0'
        """
        inputs = ['0.0']
        output = self.run_exercise(inputs)
        expected_output = "0 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Separates integer and fractional parts of '3.14159' which should be '3 14159'
        """
        inputs = ['3.14159']
        output = self.run_exercise(inputs)
        expected_output = "3 14159"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Separates integer and fractional parts of '99.999' which should be '99 999'
        """
        inputs = ['99.999']
        output = self.run_exercise(inputs)
        expected_output = "99 999"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Separates integer and fractional parts of '1.0' which should be '1 0'
        """
        inputs = ['1.0']
        output = self.run_exercise(inputs)
        expected_output = "1 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Separates integer and fractional parts of '12345.6789' which should be '12345 6789'
        """
        inputs = ['12345.6789']
        output = self.run_exercise(inputs)
        expected_output = "12345 6789"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Separates integer and fractional parts of '2.71828' which should be '2 71828'
        """
        inputs = ['2.71828']
        output = self.run_exercise(inputs)
        expected_output = "2 71828"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
