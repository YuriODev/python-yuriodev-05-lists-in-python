import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise33(CustomTestCase):

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
        Maximize number by removing one digit from 432
        """
        inputs = ['432']
        output = self.run_exercise(inputs)
        expected_output = "43"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Maximize number by removing one digit from 239
        """
        inputs = ['239']
        output = self.run_exercise(inputs)
        expected_output = "39"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Maximize number by removing one digit from 101
        """
        inputs = ['101']
        output = self.run_exercise(inputs)
        expected_output = "11"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Maximize number by removing one digit from 584
        """
        inputs = ['584']
        output = self.run_exercise(inputs)
        expected_output = "84"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Maximize number by removing one digit from 1024
        """
        inputs = ['1024']
        output = self.run_exercise(inputs)
        expected_output = "124"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Maximize number by removing one digit from 700
        """
        inputs = ['700']
        output = self.run_exercise(inputs)
        expected_output = "70"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Maximize number by removing one digit from 1234
        """
        inputs = ['1234']
        output = self.run_exercise(inputs)
        expected_output = "234"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Maximize number by removing one digit from 9001
        """
        inputs = ['9001']
        output = self.run_exercise(inputs)
        expected_output = "901"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Maximize number by removing one digit from 1111
        """
        inputs = ['1111']
        output = self.run_exercise(inputs)
        expected_output = "111"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Maximize number by removing one digit from 9090
        """
        inputs = ['9090']
        output = self.run_exercise(inputs)
        expected_output = "990"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
