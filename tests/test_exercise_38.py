import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise38(CustomTestCase):

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
        Generate smallest and largest number from 1390
        """
        inputs = ['1390']
        output = self.run_exercise(inputs)
        expected_output = "1039 9310"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Generate smallest and largest number from 1010
        """
        inputs = ['1010']
        output = self.run_exercise(inputs)
        expected_output = "1001 1100"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Generate smallest and largest number from 5173
        """
        inputs = ['5173']
        output = self.run_exercise(inputs)
        expected_output = "1357 7531"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Generate smallest and largest number from 2489
        """
        inputs = ['2489']
        output = self.run_exercise(inputs)
        expected_output = "2489 9842"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Generate smallest and largest number from 8765
        """
        inputs = ['8765']
        output = self.run_exercise(inputs)
        expected_output = "5678 8765"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Generate smallest and largest number from 1234
        """
        inputs = ['1234']
        output = self.run_exercise(inputs)
        expected_output = "1234 4321"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Generate smallest and largest number from 4321
        """
        inputs = ['4321']
        output = self.run_exercise(inputs)
        expected_output = "1234 4321"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Generate smallest and largest number from 9990
        """
        inputs = ['9990']
        output = self.run_exercise(inputs)
        expected_output = "9099 9990"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Generate smallest and largest number from 1023
        """
        inputs = ['1023']
        output = self.run_exercise(inputs)
        expected_output = "1023 3210"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Generate smallest and largest number from 4001
        """
        inputs = ['4001']
        output = self.run_exercise(inputs)
        expected_output = "1004 4100"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
