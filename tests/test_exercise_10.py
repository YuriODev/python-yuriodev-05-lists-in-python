import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise10(CustomTestCase):

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
        Counts the number of 5s in '2 5 8 19 7' which should be 1
        """
        inputs = ['2 5 8 19 7', '5']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Counts the number of 9s in '2 6 7 8 9 9 2 3' which should be 2
        """
        inputs = ['2 6 7 8 9 9 2 3', '9']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Counts the number of 6s in '1 1 2 2 3 3 4 4 5' which should be 0
        """
        inputs = ['1 1 2 2 3 3 4 4 5', '6']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Counts the number of 10s in '10 20 30 40 50' which should be 1
        """
        inputs = ['10 20 30 40 50', '10']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Counts the number of 3s in '3 3 3 3 3' which should be 5
        """
        inputs = ['3 3 3 3 3', '3']
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Counts the number of 0s in '0 0 0 0' which should be 4
        """
        inputs = ['0 0 0 0', '0']
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Counts the number of 7s in '7 14 21 7 7' which should be 3
        """
        inputs = ['7 14 21 7 7', '7']
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Counts the number of 8s in '1 2 3 4 5 6 7' which should be 0
        """
        inputs = ['1 2 3 4 5 6 7', '8']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Counts the number of 15s in '15 15 15 15' which should be 4
        """
        inputs = ['15 15 15 15', '15']
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Counts the number of 2s in '2 2 2 2 2 2' which should be 6
        """
        inputs = ['2 2 2 2 2 2', '2']
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
