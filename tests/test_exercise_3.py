import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise3(CustomTestCase):

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
        Prints even numbers from '1 2 2 3 3 3 4 4 4 4' as '2 2 4 4 4 4'
        """
        inputs = ['1 2 2 3 3 3 4 4 4 4']
        output = self.run_exercise(inputs)
        expected_output = "2 2 4 4 4 4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Prints even numbers from '7 8 10 13 14 16' as '8 10 14 16'
        """
        inputs = ['7 8 10 13 14 16']
        output = self.run_exercise(inputs)
        expected_output = "8 10 14 16"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Prints even numbers from '2 4 6 8 10' as '2 4 6 8 10'
        """
        inputs = ['2 4 6 8 10']
        output = self.run_exercise(inputs)
        expected_output = "2 4 6 8 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Prints even numbers from '1 3 5 7 9' as ''
        """
        inputs = ['1 3 5 7 9']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Prints even numbers from '0 2 4 6 8 10' as '0 2 4 6 8 10'
        """
        inputs = ['0 2 4 6 8 10']
        output = self.run_exercise(inputs)
        expected_output = "0 2 4 6 8 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Prints even numbers from '-2 -4 -6 -8' as '-2 -4 -6 -8'
        """
        inputs = ['-2 -4 -6 -8']
        output = self.run_exercise(inputs)
        expected_output = "-2 -4 -6 -8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Prints even numbers from '11 13 15 17' as ''
        """
        inputs = ['11 13 15 17']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Prints even numbers from '20 25 30 35 40' as '20 30 40'
        """
        inputs = ['20 25 30 35 40']
        output = self.run_exercise(inputs)
        expected_output = "20 30 40"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Prints even numbers from '100 101 102 103' as '100 102'
        """
        inputs = ['100 101 102 103']
        output = self.run_exercise(inputs)
        expected_output = "100 102"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Prints even numbers from '50 51 52 53 54' as '50 52 54'
        """
        inputs = ['50 51 52 53 54']
        output = self.run_exercise(inputs)
        expected_output = "50 52 54"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
