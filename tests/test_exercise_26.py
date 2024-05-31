import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise26(CustomTestCase):

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
        Rearrange even and odd numbers, basic case with mixed values
        """
        inputs = ['2 5 7 8 9 10 12 32 5']
        output = self.run_exercise(inputs)
        expected_output = "32 12 10 8 2 5 5 7 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Rearrange even and odd numbers, alternating even and odd
        """
        inputs = ['3 4 5 6 7']
        output = self.run_exercise(inputs)
        expected_output = "6 4 3 5 7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Rearrange even and odd numbers, starting with odd values
        """
        inputs = ['1 2 3 4 5']
        output = self.run_exercise(inputs)
        expected_output = "4 2 1 3 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Rearrange even and odd numbers, descending order
        """
        inputs = ['8 7 6 5 4']
        output = self.run_exercise(inputs)
        expected_output = "8 6 4 5 7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Rearrange even and odd numbers, all even
        """
        inputs = ['2 4 6 8 10']
        output = self.run_exercise(inputs)
        expected_output = "10 8 6 4 2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Rearrange even and odd numbers, all odd
        """
        inputs = ['1 3 5 7 9']
        output = self.run_exercise(inputs)
        expected_output = "1 3 5 7 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Rearrange even and odd numbers, single even
        """
        inputs = ['2']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Rearrange even and odd numbers, single odd
        """
        inputs = ['3']
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Rearrange even and odd numbers, no numbers
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Rearrange even and odd numbers, large numbers
        """
        inputs = ['1000000 999999 500000 1']
        output = self.run_exercise(inputs)
        expected_output = "1000000 500000 1 999999"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
