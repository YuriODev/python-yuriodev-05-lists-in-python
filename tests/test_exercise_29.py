import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise29(CustomTestCase):

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
        Print spiral matrix of size 4
        """
        inputs = ['4']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4\n12 13 14 5\n11 16 15 6\n10 9 8 7"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Print spiral matrix of size 3
        """
        inputs = ['3']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3\n8 9 4\n7 6 5"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Print spiral matrix of size 5
        """
        inputs = ['5']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5\n16 17 18 19 6\n15 24 25 20 7\n14 23 22 21 8\n13 12 11 10 9"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Print spiral matrix of size 2
        """
        inputs = ['2']
        output = self.run_exercise(inputs)
        expected_output = "1 2\n4 3"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Print spiral matrix of size 1
        """
        inputs = ['1']
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Print spiral matrix of size 6
        """
        inputs = ['6']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6\n20 21 22 23 24 7\n19 32 33 34 25 8\n18 31 36 35 26 9\n17 30 29 28 27 10\n16 15 14 13 12 11"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Print spiral matrix of size 7
        """
        inputs = ['7']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7\n24 25 26 27 28 29 8\n23 40 41 42 43 30 9\n22 39 48 49 44 31 10\n21 38 47 46 45 32 11\n20 37 36 35 34 33 12\n19 18 17 16 15 14 13"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Print spiral matrix of size 8
        """
        inputs = ['8']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8\n28 29 30 31 32 33 34 9\n27 48 49 50 51 52 35 10\n26 47 60 61 62 53 36 11\n25 46 59 64 63 54 37 12\n24 45 58 57 56 55 38 13\n23 44 43 42 41 40 39 14\n22 21 20 19 18 17 16 15"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Print spiral matrix of size 9
        """
        inputs = ['9']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9\n32 33 34 35 36 37 38 39 10\n31 56 57 58 59 60 61 40 11\n30 55 72 73 74 75 62 41 12\n29 54 71 80 81 76 63 42 13\n28 53 70 79 78 77 64 43 14\n27 52 69 68 67 66 65 44 15\n26 51 50 49 48 47 46 45 16\n25 24 23 22 21 20 19 18 17"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Print spiral matrix of size 10
        """
        inputs = ['10']
        output = self.run_exercise(inputs)
        expected_output = "1 2 3 4 5 6 7 8 9 10\n36 37 38 39 40 41 42 43 44 11\n35 64 65 66 67 68 69 70 45 12\n34 63 84 85 86 87 88 71 46 13\n33 62 83 96 97 98 89 72 47 14\n32 61 82 95 100 99 90 73 48 15\n31 60 81 94 93 92 91 74 49 16\n30 59 80 79 78 77 76 75 50 17\n29 58 57 56 55 54 53 52 51 18\n28 27 26 25 24 23 22 21 20 19"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
