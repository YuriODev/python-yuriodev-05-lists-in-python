import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise30(CustomTestCase):

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
        Caesar cipher with shift 2 for emojis
        """
        inputs = ['2', '😍😎😏']
        output = self.run_exercise(inputs)
        expected_output = "😏😐😑"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Caesar cipher with shift 1 for emojis
        """
        inputs = ['1', '😀😁😂']
        output = self.run_exercise(inputs)
        expected_output = "😁😂😃"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Caesar cipher with shift 3 for emojis
        """
        inputs = ['3', '😅😆😇']
        output = self.run_exercise(inputs)
        expected_output = "😈😉😊"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Caesar cipher with negative shift -1 for emojis
        """
        inputs = ['-1', '😜😝😛']
        output = self.run_exercise(inputs)
        expected_output = "😛😜😚"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Caesar cipher with large positive shift 50 for emojis
        """
        inputs = ['50', '😀😁😂']
        output = self.run_exercise(inputs)
        expected_output = "😲😳😴"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Caesar cipher with large negative shift -50 for emojis
        """
        inputs = ['-50', '😀😁😂']
        output = self.run_exercise(inputs)
        expected_output = "😞😟😠"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Caesar cipher with zero shift for emojis
        """
        inputs = ['0', '😀😁😂']
        output = self.run_exercise(inputs)
        expected_output = "😀😁😂"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Caesar cipher with shift 1 for a single emoji
        """
        inputs = ['1', '😊']
        output = self.run_exercise(inputs)
        expected_output = "😋"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Caesar cipher with negative shift -1 for a single emoji
        """
        inputs = ['-1', '😊']
        output = self.run_exercise(inputs)
        expected_output = "😉"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Caesar cipher with shift 5 for mixed emojis
        """
        inputs = ['5', '😇😍😎😜']
        output = self.run_exercise(inputs)
        expected_output = "😌😒😓😡"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
