import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise6(CustomTestCase):

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
        Counts elements greater than both neighbors in '1 2 1' which should be 1
        """
        inputs = ['1 2 1']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Counts elements greater than both neighbors in '1 3 2 4 2' which should be 2
        """
        inputs = ['1 3 2 4 2']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Counts elements greater than both neighbors in '1 2 3' which should be 0
        """
        inputs = ['1 2 3']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Counts elements greater than both neighbors in '5 4 3 2 1' which should be 0
        """
        inputs = ['5 4 3 2 1']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Counts elements greater than both neighbors in '10 20 10 5 25 5 50' which should be 2
        """
        inputs = ['10 20 10 5 25 5 50']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Counts elements greater than both neighbors in '1 1 1 1 1' which should be 0
        """
        inputs = ['1 1 1 1 1']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Counts elements greater than both neighbors in '3 2 3 2 3 2 3' which should be 2
        """
        inputs = ['3 2 3 2 3 2 3']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Counts elements greater than both neighbors in '0 0 0 0' which should be 0
        """
        inputs = ['0 0 0 0']
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Counts elements greater than both neighbors in '1 5 1 5 1' which should be 2
        """
        inputs = ['1 5 1 5 1']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Counts elements greater than both neighbors in '100 200 100 200 100' which should be 2
        """
        inputs = ['100 200 100 200 100']
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
