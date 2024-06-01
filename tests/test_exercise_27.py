import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise27(CustomTestCase):

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
        Calculate balance with a single deposit
        """
        inputs = ["1", 'D 100']
        output = self.run_exercise(inputs)
        expected_output = "100"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Calculate balance with a deposit and a withdrawal
        """
        inputs = ['2', 'D 300', 'W 100']
        output = self.run_exercise(inputs)
        expected_output = "200"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Calculate balance with multiple deposits and withdrawals
        """
        inputs = ['4', 'D 500', 'W 200', 'D 150', 'W 100']
        output = self.run_exercise(inputs)
        expected_output = "350"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Calculate balance with withdrawals exceeding deposits
        """
        inputs = ['2', 'D 100', 'W 200']
        output = self.run_exercise(inputs)
        expected_output = "-100"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Calculate balance with no transactions
        """
        inputs = ['0']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Calculate balance with only deposits
        """
        inputs = ['3', 'D 100', 'D 200', 'D 300']
        output = self.run_exercise(inputs)
        expected_output = "600"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Calculate balance with only withdrawals
        """
        inputs = ['3', 'W 100', 'W 200', 'W 50']
        output = self.run_exercise(inputs)
        expected_output = "-350"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Calculate balance with alternating deposits and withdrawals
        """
        inputs = ['4', 'D 100', 'W 50', 'D 200', 'W 150']
        output = self.run_exercise(inputs)
        expected_output = "100"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Calculate balance with small amounts
        """
        inputs = ['4', 'D 1', 'W 1', 'D 2', 'W 2']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Calculate balance with large amounts
        """
        inputs = ['4', 'D 1000000', 'W 500000', 'D 200000', 'W 100000']
        output = self.run_exercise(inputs)
        expected_output = "600000"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
