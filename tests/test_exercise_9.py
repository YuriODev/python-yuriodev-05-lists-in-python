import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise9(CustomTestCase):

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
        Converts '7,9,12,4' to a list and a tuple which should be '[7, 9, 12, 4]\n(7, 9, 12, 4)'
        """
        inputs = ['7,9,12,4']
        output = self.run_exercise(inputs)
        expected_output = "[7, 9, 12, 4]\n(7, 9, 12, 4)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Converts '1,2,3' to a list and a tuple which should be '[1, 2, 3]\n(1, 2, 3)'
        """
        inputs = ['1,2,3']
        output = self.run_exercise(inputs)
        expected_output = "[1, 2, 3]\n(1, 2, 3)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Converts '10,20,30,40' to a list and a tuple which should be '[10, 20, 30, 40]\n(10, 20, 30, 40)'
        """
        inputs = ['10,20,30,40']
        output = self.run_exercise(inputs)
        expected_output = "[10, 20, 30, 40]\n(10, 20, 30, 40)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Converts '5,6,7,8,9' to a list and a tuple which should be '[5, 6, 7, 8, 9]\n(5, 6, 7, 8, 9)'
        """
        inputs = ['5,6,7,8,9']
        output = self.run_exercise(inputs)
        expected_output = "[5, 6, 7, 8, 9]\n(5, 6, 7, 8, 9)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Converts '0,1,2,3,4' to a list and a tuple which should be '[0, 1, 2, 3, 4]\n(0, 1, 2, 3, 4)'
        """
        inputs = ['0,1,2,3,4']
        output = self.run_exercise(inputs)
        expected_output = "[0, 1, 2, 3, 4]\n(0, 1, 2, 3, 4)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Converts '100,200,300' to a list and a tuple which should be '[100, 200, 300]\n(100, 200, 300)'
        """
        inputs = ['100,200,300']
        output = self.run_exercise(inputs)
        expected_output = "[100, 200, 300]\n(100, 200, 300)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Converts '1' to a list and a tuple which should be '[1]\n(1)'
        """
        inputs = ['1']
        output = self.run_exercise(inputs)
        expected_output = "[1]\n(1,)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Converts '9,8,7,6,5' to a list and a tuple which should be '[9, 8, 7, 6, 5]\n(9, 8, 7, 6, 5)'
        """
        inputs = ['9,8,7,6,5']
        output = self.run_exercise(inputs)
        expected_output = "[9, 8, 7, 6, 5]\n(9, 8, 7, 6, 5)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Converts '10,0,0,5' to a list and a tuple which should be '[10, 0, 0, 5]\n(10, 0, 0, 5)'
        """
        inputs = ['10,0,0,5']
        output = self.run_exercise(inputs)
        expected_output = "[10, 0, 0, 5]\n(10, 0, 0, 5)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Converts '3,6,9,12' to a list and a tuple which should be '[3, 6, 9, 12]\n(3, 6, 9, 12)'
        """
        inputs = ['3,6,9,12']
        output = self.run_exercise(inputs)
        expected_output = "[3, 6, 9, 12]\n(3, 6, 9, 12)"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
