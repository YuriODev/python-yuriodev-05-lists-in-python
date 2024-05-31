import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise16(CustomTestCase):

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
        Finds unique elements in '5 3 1 6 5 8 0 12' which should be '3 1 6 8 0 12'
        """
        inputs = ['5 3 1 6 5 8 0 12']
        output = self.run_exercise(inputs)
        expected_output = "3 1 6 8 0 12"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Finds unique elements in '1 45 23 45 90 1 0' which should be '23 90 0'
        """
        inputs = ['1 45 23 45 90 1 0']
        output = self.run_exercise(inputs)
        expected_output = "23 90 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Finds unique elements in '2 3 4 2 3 5' which should be '4 5'
        """
        inputs = ['2 3 4 2 3 5']
        output = self.run_exercise(inputs)
        expected_output = "4 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Finds unique elements in '7 8 9 7 8 10' which should be '9 10'
        """
        inputs = ['7 8 9 7 8 10']
        output = self.run_exercise(inputs)
        expected_output = "9 10"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Finds unique elements in '1 1 1 2 3 4' which should be '2 3 4'
        """
        inputs = ['1 1 1 2 3 4']
        output = self.run_exercise(inputs)
        expected_output = "2 3 4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Finds unique elements in '9 8 7 6 5 4 3 2 1' which should be '9 8 7 6 5 4 3 2 1'
        """
        inputs = ['9 8 7 6 5 4 3 2 1']
        output = self.run_exercise(inputs)
        expected_output = "9 8 7 6 5 4 3 2 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Finds unique elements in '10 20 30 20 10' which should be '30'
        """
        inputs = ['10 20 30 20 10']
        output = self.run_exercise(inputs)
        expected_output = "30"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Finds unique elements in '1 2 3 4 5 6 7 8 9 0' which should be '1 2 3 4 5 6 7 8 9 0'
        """
        inputs = ['1 2 3 4 5 6 7 8 9 0']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Finds unique elements in '11 22 33 44 55 11 22 33' which should be '44 55'
        """
        inputs = ['11 22 33 44 55 11 22 33']
        output = self.run_exercise(inputs)
        expected_output = "44 55"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Finds unique elements in '5 4 3 2 1 2 3 4' which should be '5 1'
        """
        inputs = ['5 4 3 2 1 2 3 4']
        output = self.run_exercise(inputs)
        expected_output = "5 1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
