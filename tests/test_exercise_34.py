import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise34(CustomTestCase):

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
        Find the longest word in a short sentence
        """
        inputs = ['Sparse is better than dense']
        output = self.run_exercise(inputs)
        expected_output = "Sparse better"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Find the longest word in a simple sentence
        """
        inputs = ['Readability counts']
        output = self.run_exercise(inputs)
        expected_output = "Readability"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Find the longest words in a complex sentence
        """
        inputs = ["Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for Python's design into 20 aphorisms"]
        output = self.run_exercise(inputs)
        expected_output = "succinctly principles"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Find the longest word in a basic sentence
        """
        inputs = ['This is a simple test']
        output = self.run_exercise(inputs)
        expected_output = "simple"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Find the longest word in a sentence with multiple longest words
        """
        inputs = ['We all love Python programming']
        output = self.run_exercise(inputs)
        expected_output = "programming"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Find the longest word in a single word sentence
        """
        inputs = ['Supercalifragilisticexpialidocious']
        output = self.run_exercise(inputs)
        expected_output = "Supercalifragilisticexpialidocious"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Find the longest word in a sentence with equal length words
        """
        inputs = ['cat bat rat']
        output = self.run_exercise(inputs)
        expected_output = "cat bat rat"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Find the longest word in a sentence with mixed length words
        """
        inputs = ['Python is amazing and incredibly versatile']
        output = self.run_exercise(inputs)
        expected_output = "incredibly"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Find the longest word in a sentence with numbers and words
        """
        inputs = ['Python 3.8 is awesome']
        output = self.run_exercise(inputs)
        expected_output = "awesome"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Find the longest word in a sentence with punctuation
        """
        inputs = ['Hello, world! Programming is fun.']
        output = self.run_exercise(inputs)
        expected_output = "Programming"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
