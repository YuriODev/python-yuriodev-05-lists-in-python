import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise5(CustomTestCase):

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
        Counts unique elements in '5 7 7 9 12' which should be 4
        """
        inputs = ['5 7 7 9 12']
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Counts unique elements in '1 2 3 4 5' which should be 5
        """
        inputs = ['1 2 3 4 5']
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Counts unique elements in '3 3 3 3 3' which should be 1
        """
        inputs = ['3 3 3 3 3']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Counts unique elements in '10 20 30 20 10' which should be 3
        """
        inputs = ['10 20 30 20 10']
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Counts unique elements in '7 7 7 7 7 7 7' which should be 1
        """
        inputs = ['7 7 7 7 7 7 7']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Counts unique elements in '1 1 2 2 3 3' which should be 3
        """
        inputs = ['1 1 2 2 3 3']
        output = self.run_exercise(inputs)
        expected_output = "3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Counts unique elements in '0 0 0 0 0' which should be 1
        """
        inputs = ['0 0 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Counts unique elements in '4 5 6 6 5 4 3 2 1' which should be 6
        """
        inputs = ['4 5 6 6 5 4 3 2 1']
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Counts unique elements in '100 200 300 400 500' which should be 5
        """
        inputs = ['100 200 300 400 500']
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Counts unique elements in '50 50 50 50 50 50' which should be 1
        """
        inputs = ['50 50 50 50 50 50']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
