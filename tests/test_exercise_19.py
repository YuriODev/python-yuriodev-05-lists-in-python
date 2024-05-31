import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise19(CustomTestCase):

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
        Converts 'my_class' to 'MyClass'
        """
        inputs = ['my_class']
        output = self.run_exercise(inputs)
        expected_output = "MyClass"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Converts 'this_is_a_test' to 'ThisIsATest'
        """
        inputs = ['this_is_a_test']
        output = self.run_exercise(inputs)
        expected_output = "ThisIsATest"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Converts 'convert_to_camel' to 'ConvertToCamel'
        """
        inputs = ['convert_to_camel']
        output = self.run_exercise(inputs)
        expected_output = "ConvertToCamel"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Converts 'example_string' to 'ExampleString'
        """
        inputs = ['example_string']
        output = self.run_exercise(inputs)
        expected_output = "ExampleString"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Converts 'underscore_to_camelcase' to 'UnderscoreToCamelcase'
        """
        inputs = ['underscore_to_camelcase']
        output = self.run_exercise(inputs)
        expected_output = "UnderscoreToCamelcase"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Converts 'convert_me' to 'ConvertMe'
        """
        inputs = ['convert_me']
        output = self.run_exercise(inputs)
        expected_output = "ConvertMe"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Converts 'test_example_case' to 'TestExampleCase'
        """
        inputs = ['test_example_case']
        output = self.run_exercise(inputs)
        expected_output = "TestExampleCase"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Converts 'python_script' to 'PythonScript'
        """
        inputs = ['python_script']
        output = self.run_exercise(inputs)
        expected_output = "PythonScript"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Converts 'java_to_python' to 'JavaToPython'
        """
        inputs = ['java_to_python']
        output = self.run_exercise(inputs)
        expected_output = "JavaToPython"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Converts 'camel_case_conversion' to 'CamelCaseConversion'
        """
        inputs = ['camel_case_conversion']
        output = self.run_exercise(inputs)
        expected_output = "CamelCaseConversion"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
