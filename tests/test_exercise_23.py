import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise23(CustomTestCase):

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
        Reverses digits [1, 4, 8, 3, 9, 5] to form 593841
        """
        inputs = ['1 4 8 3 9 5']
        output = self.run_exercise(inputs)
        expected_output = "985431"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Reverses digits [2, 1, 3] to form 321
        """
        inputs = ['2 1 3']
        output = self.run_exercise(inputs)
        expected_output = "321"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Reverses digits [7, 0, 5, 4] to form 7540
        """
        inputs = ['7 0 5 4']
        output = self.run_exercise(inputs)
        expected_output = "7540"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Reverses digits [9, 8, 7, 6, 5] to form 98765
        """
        inputs = ['9 8 7 6 5']
        output = self.run_exercise(inputs)
        expected_output = "98765"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Reverses digits [5, 3, 1] to form 531
        """
        inputs = ['5 3 1']
        output = self.run_exercise(inputs)
        expected_output = "531"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Reverses digits [0, 2, 4] to form 420
        """
        inputs = ['0 2 4']
        output = self.run_exercise(inputs)
        expected_output = "420"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Reverses digits [1, 2, 2, 1] to form 1221
        """
        inputs = ['1 2 2 1']
        output = self.run_exercise(inputs)
        expected_output = "2211"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Reverses digits [3, 6, 9] to form 963
        """
        inputs = ['3 6 9']
        output = self.run_exercise(inputs)
        expected_output = "963"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Reverses digits [4, 5, 6, 7, 8, 9] to form 987654
        """
        inputs = ['4 5 6 7 8 9']
        output = self.run_exercise(inputs)
        expected_output = "987654"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Reverses digits [2, 4, 6, 8] to form 8642
        """
        inputs = ['2 4 6 8']
        output = self.run_exercise(inputs)
        expected_output = "8642"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
