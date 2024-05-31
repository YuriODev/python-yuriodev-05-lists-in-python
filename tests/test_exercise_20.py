import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise20(CustomTestCase):

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
        Finds the first letter of the word at position 3 in 'Now is better than never' which should be 'b'
        """
        inputs = ['Now is better than never', '3']
        output = self.run_exercise(inputs)
        expected_output = "b"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Finds the first letter of the word at position 2 in 'Hello world from Python' which should be 'w'
        """
        inputs = ['Hello world from Python', '2']
        output = self.run_exercise(inputs)
        expected_output = "w"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Finds the first letter of the word at position 4 in 'This is a sample text' which should be 's'
        """
        inputs = ['This is a sample text', '4']
        output = self.run_exercise(inputs)
        expected_output = "s"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Finds the first letter of the word at position 2 in 'Find the first letter here' which should be 't'
        """
        inputs = ['Find the first letter here', '2']
        output = self.run_exercise(inputs)
        expected_output = "t"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Finds the first letter of the word at position 4 in 'Python is fun and powerful' which should be 'p'
        """
        inputs = ['Python is fun and powerful', '4']
        output = self.run_exercise(inputs)
        expected_output = "a"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Finds the first letter of the word at position 3 in 'I love programming' which should be 'p'
        """
        inputs = ['I love programming', '3']
        output = self.run_exercise(inputs)
        expected_output = "p"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Finds the first letter of the word at position 3 in 'JavaScript is also cool' which should be 'a'
        """
        inputs = ['JavaScript is also cool', '3']
        output = self.run_exercise(inputs)
        expected_output = "a"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Finds the first letter of the word at position 4 in 'Data science is amazing' which should be 'a'
        """
        inputs = ['Data science is amazing', '4']
        output = self.run_exercise(inputs)
        expected_output = "a"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Finds the first letter of the word at position 2 in 'Learning new skills' which should be 'n'
        """
        inputs = ['Learning new skills', '2']
        output = self.run_exercise(inputs)
        expected_output = "n"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Finds the first letter of the word at position 4 in 'Reading books is fun' which should be 'f'
        """
        inputs = ['Reading books is fun', '4']
        output = self.run_exercise(inputs)
        expected_output = "f"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
