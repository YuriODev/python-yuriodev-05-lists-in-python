import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise21(CustomTestCase):

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
        Inserts 0 at index 3 in the list [9, 4, 6, 2, 0, 7, 14], resulting in [9, 4, 6, 0, 2, 0, 7, 14]
        """
        inputs = ['9 4 6 2 0 7 14', '3', '0']
        output = self.run_exercise(inputs)
        expected_output = "9 4 6 0 2 0 7 14"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Inserts 0 at index 2 in the list [1, 2, 3, 4, 5], resulting in [1, 2, 0, 3, 4, 5]
        """
        inputs = ['1 2 3 4 5', '2', '0']
        output = self.run_exercise(inputs)
        expected_output = "1 2 0 3 4 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Inserts 0 at index 3 in the list [10, 20, 30, 40, 50], resulting in [10, 20, 30, 0, 40, 50]
        """
        inputs = ['10 20 30 40 50', '3', '0']
        output = self.run_exercise(inputs)
        expected_output = "10 20 30 0 40 50"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Inserts 0 at index 1 in the list [5, 6, 7, 8], resulting in [5, 0, 6, 7, 8]
        """
        inputs = ['5 6 7 8', '1', '0']
        output = self.run_exercise(inputs)
        expected_output = "5 0 6 7 8"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Inserts 7 at index 0 in the list [1, 2, 3], resulting in [7, 1, 2, 3]
        """
        inputs = ['1 2 3', '0', '7']
        output = self.run_exercise(inputs)
        expected_output = "7 1 2 3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Inserts 100 at index 5 in the list [10, 20, 30, 40, 50], resulting in [10, 20, 30, 40, 50, 100]
        """
        inputs = ['10 20 30 40 50', '5', '100']
        output = self.run_exercise(inputs)
        expected_output = "10 20 30 40 50 100"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Inserts 1 at index 3 in the list [3, 3, 3, 3], resulting in [3, 3, 3, 1, 3]
        """
        inputs = ['3 3 3 3', '3', '1']
        output = self.run_exercise(inputs)
        expected_output = "3 3 3 1 3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Inserts 0 at index 2 in the list [5, 10, 15, 20], resulting in [5, 10, 0, 15, 20]
        """
        inputs = ['5 10 15 20', '2', '0']
        output = self.run_exercise(inputs)
        expected_output = "5 10 0 15 20"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Inserts 6 at index 4 in the list [2, 4, 6, 8], resulting in [2, 4, 6, 8, 6]
        """
        inputs = ['2 4 6 8', '4', '6']
        output = self.run_exercise(inputs)
        expected_output = "2 4 6 8 6"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Inserts 12 at index 1 in the list [1, 2, 3], resulting in [1, 12, 2, 3]
        """
        inputs = ['1 2 3', '1', '12']
        output = self.run_exercise(inputs)
        expected_output = "1 12 2 3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
