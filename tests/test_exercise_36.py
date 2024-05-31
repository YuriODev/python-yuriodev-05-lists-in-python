import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise36(CustomTestCase):

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
        Find all positions of the number 4 in the list
        """
        inputs = ['5 7 3 4 9 8 4 7 4', '4']
        output = self.run_exercise(inputs)
        expected_output = "4 7 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Find position of the number 5 in the list
        """
        inputs = ['1 2 3 4 5 6 7 8 9', '5']
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Number not found in the list
        """
        inputs = ['10 20 30 40 50 60', '25']
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Find position of the number 66 in the list
        """
        inputs = ['11 22 33 44 55 66 77 88', '66']
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Find all positions of the number 1 in the list with duplicates
        """
        inputs = ['1 1 1 1 1 1 1 1 1 1', '1']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Find all positions of the number 0 in the list with multiple zeros
        """
        inputs = ['0 0 0 0 0 0 0 0 0 0', '0']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Find position of the number 100 in the list
        """
        inputs = ['10 20 30 40 50 60 70 80 90 100', '100']
        output = self.run_exercise(inputs)
        expected_output = "10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Number not found in the list with mixed elements
        """
        inputs = ['5 10 15 20 25 30 35 40 45 50', '60']
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Find position of the number 3 in the list with only one element
        """
        inputs = ['3', '3']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Number not found in the list with only one element
        """
        inputs = ['3', '4']
        output = self.run_exercise(inputs)
        expected_output = "None"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
