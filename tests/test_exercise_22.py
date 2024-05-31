import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise22(CustomTestCase):

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
        Converts binary 1001 to decimal 9
        """
        inputs = ['1001']
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Converts binary 101010111 to decimal 343
        """
        inputs = ['101010111']
        output = self.run_exercise(inputs)
        expected_output = "343"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Converts binary 10000 to decimal 16
        """
        inputs = ['10000']
        output = self.run_exercise(inputs)
        expected_output = "16"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Converts binary 111 to decimal 7
        """
        inputs = ['111']
        output = self.run_exercise(inputs)
        expected_output = "7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Converts binary 0 to decimal 0
        """
        inputs = ['0']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Converts binary 1 to decimal 1
        """
        inputs = ['1']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Converts binary 101 to decimal 5
        """
        inputs = ['101']
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Converts binary 1111 to decimal 15
        """
        inputs = ['1111']
        output = self.run_exercise(inputs)
        expected_output = "15"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Converts binary 1001101 to decimal 77
        """
        inputs = ['1001101']
        output = self.run_exercise(inputs)
        expected_output = "77"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Converts binary 1100100 to decimal 100
        """
        inputs = ['1100100']
        output = self.run_exercise(inputs)
        expected_output = "100"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
