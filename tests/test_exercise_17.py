import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise17(CustomTestCase):

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
        Formats '4, 3, 2019' to '4/3/2019'
        """
        inputs = ['4, 3, 2019']
        output = self.run_exercise(inputs)
        expected_output = "4/3/2019"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Formats '12, 5, 2020' to '12/5/2020'
        """
        inputs = ['12, 5, 2020']
        output = self.run_exercise(inputs)
        expected_output = "12/5/2020"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Formats '25, 12, 2021' to '25/12/2021'
        """
        inputs = ['25, 12, 2021']
        output = self.run_exercise(inputs)
        expected_output = "25/12/2021"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Formats '1, 1, 2022' to '1/1/2022'
        """
        inputs = ['1, 1, 2022']
        output = self.run_exercise(inputs)
        expected_output = "1/1/2022"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Formats '10, 11, 2023' to '10/11/2023'
        """
        inputs = ['10, 11, 2023']
        output = self.run_exercise(inputs)
        expected_output = "10/11/2023"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Formats '5, 6, 2018' to '5/6/2018'
        """
        inputs = ['5, 6, 2018']
        output = self.run_exercise(inputs)
        expected_output = "5/6/2018"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Formats '20, 10, 2017' to '20/10/2017'
        """
        inputs = ['20, 10, 2017']
        output = self.run_exercise(inputs)
        expected_output = "20/10/2017"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Formats '7, 8, 2025' to '7/8/2025'
        """
        inputs = ['7, 8, 2025']
        output = self.run_exercise(inputs)
        expected_output = "7/8/2025"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Formats '15, 4, 2026' to '15/4/2026'
        """
        inputs = ['15, 4, 2026']
        output = self.run_exercise(inputs)
        expected_output = "15/4/2026"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Formats '2, 2, 2024' to '2/2/2024'
        """
        inputs = ['2, 2, 2024']
        output = self.run_exercise(inputs)
        expected_output = "2/2/2024"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
