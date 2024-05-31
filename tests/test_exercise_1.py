import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise1(CustomTestCase):

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
        Sorts languages alphabetically in 'Ukrainian French Bulgarian Norwegian Latvian' which should be 'Bulgarian French Latvian Norwegian Ukrainian'
        """
        inputs = ['Ukrainian French Bulgarian Norwegian Latvian']
        output = self.run_exercise(inputs)
        expected_output = "Bulgarian French Latvian Norwegian Ukrainian"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Sorts languages alphabetically in 'English German Spanish Italian French' which should be 'English French German Italian Spanish'
        """
        inputs = ['English German Spanish Italian French']
        output = self.run_exercise(inputs)
        expected_output = "English French German Italian Spanish"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Sorts languages alphabetically in 'Russian Ukrainian Belarusian Polish' which should be 'Belarusian Polish Russian Ukrainian'
        """
        inputs = ['Russian Ukrainian Belarusian Polish']
        output = self.run_exercise(inputs)
        expected_output = "Belarusian Polish Russian Ukrainian"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Sorts languages alphabetically in 'English French German Italian Spanish' which should be 'English French German Italian Spanish'
        """
        inputs = ['English French German Italian Spanish']
        output = self.run_exercise(inputs)
        expected_output = "English French German Italian Spanish"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Sorts languages alphabetically in 'Zulu Xhosa Afrikaans' which should be 'Afrikaans Xhosa Zulu'
        """
        inputs = ['Zulu Xhosa Afrikaans']
        output = self.run_exercise(inputs)
        expected_output = "Afrikaans Xhosa Zulu"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Sorts languages alphabetically in 'Mandarin Cantonese Hokkien' which should be 'Cantonese Hokkien Mandarin'
        """
        inputs = ['Mandarin Cantonese Hokkien']
        output = self.run_exercise(inputs)
        expected_output = "Cantonese Hokkien Mandarin"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Sorts languages alphabetically in 'Hindi Tamil Telugu Marathi' which should be 'Hindi Marathi Tamil Telugu'
        """
        inputs = ['Hindi Tamil Telugu Marathi']
        output = self.run_exercise(inputs)
        expected_output = "Hindi Marathi Tamil Telugu"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Sorts languages alphabetically in 'Japanese Korean Chinese' which should be 'Chinese Japanese Korean'
        """
        inputs = ['Japanese Korean Chinese']
        output = self.run_exercise(inputs)
        expected_output = "Chinese Japanese Korean"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Sorts languages alphabetically in 'Portuguese Spanish Catalan' which should be 'Catalan Portuguese Spanish'
        """
        inputs = ['Portuguese Spanish Catalan']
        output = self.run_exercise(inputs)
        expected_output = "Catalan Portuguese Spanish"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Sorts languages alphabetically in 'Swedish Norwegian Danish' which should be 'Danish Norwegian Swedish'
        """
        inputs = ['Swedish Norwegian Danish']
        output = self.run_exercise(inputs)
        expected_output = "Danish Norwegian Swedish"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
