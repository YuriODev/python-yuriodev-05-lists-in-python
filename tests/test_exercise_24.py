import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise24(CustomTestCase):

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
        Arranges numbers [1, 3, -5, 0, 10, -2, 12, 45, 7, 0, 9, -4, -11, 15, 22, 3] with positives in descending and negatives at the end
        """
        inputs = ['1 3 -5 0 10 -2 12 45 7 0 9 -4 -11 15 22 3']
        output = self.run_exercise(inputs)
        expected_output = "45 22 15 12 10 9 7 3 3 1 -2 -4 -5 -11"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Arranges numbers [5, -3, 6, -2, 7, 0, -1, 8] with positives in descending and negatives at the end
        """
        inputs = ['5 -3 6 -2 7 0 -1 8']
        output = self.run_exercise(inputs)
        expected_output = "8 7 6 5 -1 -2 -3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Arranges numbers [2, -4, -6, 4, 3] with positives in descending and negatives at the end
        """
        inputs = ['2 -4 -6 4 3']
        output = self.run_exercise(inputs)
        expected_output = "4 3 2 -4 -6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Arranges numbers [-7, -8, 9, 0, 10, 11, -9] with positives in descending and negatives at the end
        """
        inputs = ['-7 -8 9 0 10 11 -9']
        output = self.run_exercise(inputs)
        expected_output = "11 10 9 -7 -8 -9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Arranges numbers [10, -10, 20, -20, 30, -30] with positives in descending and negatives at the end
        """
        inputs = ['10 -10 20 -20 30 -30']
        output = self.run_exercise(inputs)
        expected_output = "30 20 10 -10 -20 -30"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Arranges numbers [1, -1, 2, -2, 3, -3] with positives in descending and negatives at the end
        """
        inputs = ['1 -1 2 -2 3 -3']
        output = self.run_exercise(inputs)
        expected_output = "3 2 1 -1 -2 -3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Arranges numbers [0, 0, 0, -1, -2, -3] with positives in descending and negatives at the end
        """
        inputs = ['0 0 0 -1 -2 -3']
        output = self.run_exercise(inputs)
        expected_output = "-1 -2 -3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Arranges numbers [4, 3, 2, 1, 0, -1, -2, -3, -4] with positives in descending and negatives at the end
        """
        inputs = ['4 3 2 1 0 -1 -2 -3 -4']
        output = self.run_exercise(inputs)
        expected_output = "4 3 2 1 -1 -2 -3 -4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Arranges numbers [-5, -4, -3, -2, -1] with positives in descending and negatives at the end
        """
        inputs = ['-5 -4 -3 -2 -1']
        output = self.run_exercise(inputs)
        expected_output = "-1 -2 -3 -4 -5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Arranges numbers [6, -6, 7, -7, 8, -8] with positives in descending and negatives at the end
        """
        inputs = ['6 -6 7 -7 8 -8']
        output = self.run_exercise(inputs)
        expected_output = "8 7 6 -6 -7 -8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
