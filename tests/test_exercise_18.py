import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise18(CustomTestCase):

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
        Swaps min and max in '5 6 8 1 4 9 12' which should be '5 6 8 12 4 9 1'
        """
        inputs = ['5 6 8 1 4 9 12']
        output = self.run_exercise(inputs)
        expected_output = "5 6 8 12 4 9 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Swaps min and max in '2 3 1 5 4' which should be '2 3 5 1 4'
        """
        inputs = ['2 3 1 5 4']
        output = self.run_exercise(inputs)
        expected_output = "2 3 5 1 4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Swaps min and max in '7 6 5 4 3' which should be '3 6 5 4 7'
        """
        inputs = ['7 6 5 4 3']
        output = self.run_exercise(inputs)
        expected_output = "3 6 5 4 7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Swaps min and max in '10 20 30 40 50' which should be '50 20 30 40 10'
        """
        inputs = ['10 20 30 40 50']
        output = self.run_exercise(inputs)
        expected_output = "50 20 30 40 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Swaps min and max in '5 3 9 1 7' which should be '5 3 1 9 7'
        """
        inputs = ['5 3 9 1 7']
        output = self.run_exercise(inputs)
        expected_output = "5 3 1 9 7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Swaps min and max in '15 25 35 45 55' which should be '55 25 35 45 15'
        """
        inputs = ['15 25 35 45 55']
        output = self.run_exercise(inputs)
        expected_output = "55 25 35 45 15"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Swaps min and max in '7 8 9 10 1' which should be '7 8 9 1 10'
        """
        inputs = ['7 8 9 10 1']
        output = self.run_exercise(inputs)
        expected_output = "7 8 9 1 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Swaps min and max in '4 5 6 3 2' which should be '4 5 2 3 6'
        """
        inputs = ['4 5 6 3 2']
        output = self.run_exercise(inputs)
        expected_output = "4 5 2 3 6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Swaps min and max in '12 11 10 9 8' which should be '8 11 10 9 12'
        """
        inputs = ['12 11 10 9 8']
        output = self.run_exercise(inputs)
        expected_output = "8 11 10 9 12"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Swaps min and max in '22 33 44 55 66' which should be '66 33 44 55 22'
        """
        inputs = ['22 33 44 55 66']
        output = self.run_exercise(inputs)
        expected_output = "66 33 44 55 22"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
