import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise2(CustomTestCase):

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
        Sorts and reverses the list of languages from 'Ukrainian French Bulgarian Norwegian Latvian' to 'Ukrainian Norwegian Latvian French Bulgarian'
        """
        inputs = ['Ukrainian French Bulgarian Norwegian Latvian']
        output = self.run_exercise(inputs)
        expected_output = "Ukrainian Norwegian Latvian French Bulgarian"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Sorts and reverses the list of languages from 'English German Spanish Italian French' to 'Spanish Italian German French English'
        """
        inputs = ['English German Spanish Italian French']
        output = self.run_exercise(inputs)
        expected_output = "Spanish Italian German French English"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Sorts and reverses the list of languages from 'Russian Ukrainian Belarusian Polish' to 'Ukrainian Russian Polish Belarusian'
        """
        inputs = ['Russian Ukrainian Belarusian Polish']
        output = self.run_exercise(inputs)
        expected_output = "Ukrainian Russian Polish Belarusian"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Sorts and reverses the list of languages from 'English French German Italian Spanish' to 'Spanish Italian German French English'
        """
        inputs = ['English French German Italian Spanish']
        output = self.run_exercise(inputs)
        expected_output = "Spanish Italian German French English"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Sorts and reverses a single language 'English' to 'English'
        """
        inputs = ['English']
        output = self.run_exercise(inputs)
        expected_output = "English"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Sorts and reverses an empty input to an empty output
        """
        inputs = ['']
        output = self.run_exercise(inputs)
        expected_output = ""
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Sorts and reverses the list of languages from 'A B C D' to 'D C B A'
        """
        inputs = ['A B C D']
        output = self.run_exercise(inputs)
        expected_output = "D C B A"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Sorts and reverses the list of languages from 'One Two Three' to 'Two Three One'
        """
        inputs = ['One Two Three']
        output = self.run_exercise(inputs)
        expected_output = "Two Three One"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Sorts and reverses the list of languages from 'Java Python C++' to 'Python Java C++'
        """
        inputs = ['Java Python C++']
        output = self.run_exercise(inputs)
        expected_output = "Python Java C++"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Sorts and reverses the list of languages from 'Alpha Beta Gamma Delta' to 'Gamma Delta Beta Alpha'
        """
        inputs = ['Alpha Beta Gamma Delta']
        output = self.run_exercise(inputs)
        expected_output = "Gamma Delta Beta Alpha"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
