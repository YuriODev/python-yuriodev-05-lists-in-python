import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise37(CustomTestCase):

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
        Decode run-length encoded string 3ab4c2CaB
        """
        inputs = ['3ab4c2CaB']
        output = self.run_exercise(inputs)
        expected_output = "aaabccccCCaB"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Decode run-length encoded string 10a3b2c4DFj5h
        """
        inputs = ['10a3b2c4DFj5h']
        output = self.run_exercise(inputs)
        expected_output = "aaaaaaaaaabbbccDDDDFjhhhhh"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Decode run-length encoded string 5x2y3z
        """
        inputs = ['5x2y3z']
        output = self.run_exercise(inputs)
        expected_output = "xxxxxyyz"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Decode run-length encoded string 2A3B4C
        """
        inputs = ['2A3B4C']
        output = self.run_exercise(inputs)
        expected_output = "AABBBCCCC"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Decode run-length encoded string with single characters
        """
        inputs = ['a1b1c1d']
        output = self.run_exercise(inputs)
        expected_output = "abcd"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Decode run-length encoded string with no numbers
        """
        inputs = ['abcde']
        output = self.run_exercise(inputs)
        expected_output = "abcde"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Decode run-length encoded string with large numbers
        """
        inputs = ['100a2b3c']
        output = self.run_exercise(inputs)
        expected_output = 100*"a" + 2*"b" + 3*"c"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Decode run-length encoded string with mixed case letters
        """
        inputs = ['3a2B4C']
        output = self.run_exercise(inputs)
        expected_output = "aaaBBCCCC"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Decode run-length encoded string with digits as characters
        """
        inputs = ['2a3b2C4d']
        output = self.run_exercise(inputs)
        expected_output = "aabbbCCdddd"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Decode run-length encoded string with leading numbers
        """
        inputs = ['10a']
        output = self.run_exercise(inputs)
        expected_output = "aaaaaaaaaa"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
