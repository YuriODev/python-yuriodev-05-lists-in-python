import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise25(CustomTestCase):

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
        Creates a snowflake pattern for n=7
        """
        inputs = ['7']
        output = self.run_exercise(inputs)
        expected_output = """* . . * . . *
. * . * . * .
. . * * * . .
* * * * * * *
. . * * * . .
. * . * . * .
* . . * . . *"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Creates a snowflake pattern for n=5
        """
        inputs = ['5']
        output = self.run_exercise(inputs)
        expected_output = """* . * . *
. * * * .
* * * * *
. * * * .
* . * . *"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Creates a snowflake pattern for n=3
        """
        inputs = ['3']
        output = self.run_exercise(inputs)
        expected_output = """* * *
* * *
* * *"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Creates a snowflake pattern for n=1
        """
        inputs = ['1']
        output = self.run_exercise(inputs)
        expected_output = """*"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Creates a snowflake pattern for n=9
        """
        inputs = ['9']
        output = self.run_exercise(inputs)
        expected_output = """* . . . * . . . *
. * . . * . . * .
. . * . * . * . .
. . . * * * . . .
* * * * * * * * *
. . . * * * . . .
. . * . * . * . .
. * . . * . . * .
* . . . * . . . *"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Creates a snowflake pattern for n=11
        """
        inputs = ['11']
        output = self.run_exercise(inputs)
        expected_output = """* . . . . * . . . . *
. * . . . * . . . * .
. . * . . * . . * . .
. . . * . * . * . . .
. . . . * * * . . . .
* * * * * * * * * * *
. . . . * * * . . . .
. . . * . * . * . . .
. . * . . * . . * . .
. * . . . * . . . * .
* . . . . * . . . . *"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Creates a snowflake pattern for n=13
        """
        inputs = ['13']
        output = self.run_exercise(inputs)
        expected_output = """* . . . . . * . . . . . *
. * . . . . * . . . . * .
. . * . . . * . . . * . .
. . . * . . * . . * . . .
. . . . * . * . * . . . .
. . . . . * * * . . . . .
* * * * * * * * * * * * *
. . . . . * * * . . . . .
. . . . * . * . * . . . .
. . . * . . * . . * . . .
. . * . . . * . . . * . .
. * . . . . * . . . . * .
* . . . . . * . . . . . *"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Creates a snowflake pattern for n=17
        """
        inputs = ['17']
        output = self.run_exercise(inputs)
        expected_output = """* . . . . . . . * . . . . . . . *
. * . . . . . . * . . . . . . * .
. . * . . . . . * . . . . . * . .
. . . * . . . . * . . . . * . . .
. . . . * . . . * . . . * . . . .
. . . . . * . . * . . * . . . . .
. . . . . . * . * . * . . . . . .
. . . . . . . * * * . . . . . . .
* * * * * * * * * * * * * * * * *
. . . . . . . * * * . . . . . . .
. . . . . . * . * . * . . . . . .
. . . . . * . . * . . * . . . . .
. . . . * . . . * . . . * . . . .
. . . * . . . . * . . . . * . . .
. . * . . . . . * . . . . . * . .
. * . . . . . . * . . . . . . * .
* . . . . . . . * . . . . . . . *"""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
