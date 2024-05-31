import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise15(CustomTestCase):

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
        Sorts 'one,moment,please' alphabetically which should be 'moment,one,please'
        """
        inputs = ['one,moment,please']
        output = self.run_exercise(inputs)
        expected_output = "moment,one,please"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Sorts 'banana,apple,kiwi' alphabetically which should be 'apple,banana,kiwi'
        """
        inputs = ['banana,apple,kiwi']
        output = self.run_exercise(inputs)
        expected_output = "apple,banana,kiwi"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Sorts 'sun,moon,star' alphabetically which should be 'moon,star,sun'
        """
        inputs = ['sun,moon,star']
        output = self.run_exercise(inputs)
        expected_output = "moon,star,sun"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Sorts 'dog,cat,bird' alphabetically which should be 'bird,cat,dog'
        """
        inputs = ['dog,cat,bird']
        output = self.run_exercise(inputs)
        expected_output = "bird,cat,dog"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Sorts 'zebra,apple,mango' alphabetically which should be 'apple,mango,zebra'
        """
        inputs = ['zebra,apple,mango']
        output = self.run_exercise(inputs)
        expected_output = "apple,mango,zebra"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Sorts 'grape,orange,banana' alphabetically which should be 'banana,grape,orange'
        """
        inputs = ['grape,orange,banana']
        output = self.run_exercise(inputs)
        expected_output = "banana,grape,orange"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Sorts 'lemon,lime,apple' alphabetically which should be 'apple,lemon,lime'
        """
        inputs = ['lemon,lime,apple']
        output = self.run_exercise(inputs)
        expected_output = "apple,lemon,lime"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Sorts 'strawberry,blueberry,raspberry' alphabetically which should be 'blueberry,raspberry,strawberry'
        """
        inputs = ['strawberry,blueberry,raspberry']
        output = self.run_exercise(inputs)
        expected_output = "blueberry,raspberry,strawberry"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Sorts 'fig,date,pear' alphabetically which should be 'date,fig,pear'
        """
        inputs = ['fig,date,pear']
        output = self.run_exercise(inputs)
        expected_output = "date,fig,pear"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Sorts 'carrot,lettuce,cucumber' alphabetically which should be 'carrot,cucumber,lettuce'
        """
        inputs = ['carrot,lettuce,cucumber']
        output = self.run_exercise(inputs)
        expected_output = "carrot,cucumber,lettuce"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
