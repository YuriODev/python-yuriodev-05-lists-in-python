import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise11(CustomTestCase):

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
        Extracts the resource name from 'https://www.namesite.com/folder/index.html' which should be 'index.html'
        """
        inputs = ['https://www.namesite.com/folder/index.html']
        output = self.run_exercise(inputs)
        expected_output = "index.html"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        Extracts the resource name from 'http://example.com/page.html' which should be 'page.html'
        """
        inputs = ['http://example.com/page.html']
        output = self.run_exercise(inputs)
        expected_output = "page.html"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        Extracts the resource name from 'https://domain.com/path/to/resource' which should be 'resource'
        """
        inputs = ['https://domain.com/path/to/resource']
        output = self.run_exercise(inputs)
        expected_output = "resource"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        Extracts the resource name from 'http://sub.domain.com/resource/file.txt' which should be 'file.txt'
        """
        inputs = ['http://sub.domain.com/resource/file.txt']
        output = self.run_exercise(inputs)
        expected_output = "file.txt"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        Extracts the resource name from 'https://www.example.com/path/index.php' which should be 'index.php'
        """
        inputs = ['https://www.example.com/path/index.php']
        output = self.run_exercise(inputs)
        expected_output = "index.php"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_6(self):
        """
        Extracts the resource name from 'http://testsite.com/abc/def/ghi' which should be 'ghi'
        """
        inputs = ['http://testsite.com/abc/def/ghi']
        output = self.run_exercise(inputs)
        expected_output = "ghi"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_7(self):
        """
        Extracts the resource name from 'https://xyz.com/something.html' which should be 'something.html'
        """
        inputs = ['https://xyz.com/something.html']
        output = self.run_exercise(inputs)
        expected_output = "something.html"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_8(self):
        """
        Extracts the resource name from 'http://abc.com/folder/document.pdf' which should be 'document.pdf'
        """
        inputs = ['http://abc.com/folder/document.pdf']
        output = self.run_exercise(inputs)
        expected_output = "document.pdf"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_9(self):
        """
        Extracts the resource name from 'https://site.org/long/path/to/file' which should be 'file'
        """
        inputs = ['https://site.org/long/path/to/file']
        output = self.run_exercise(inputs)
        expected_output = "file"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_10(self):
        """
        Extracts the resource name from 'http://example.net/a/b/c/d/e/f/g/h.html' which should be 'h.html'
        """
        inputs = ['http://example.net/a/b/c/d/e/f/g/h.html']
        output = self.run_exercise(inputs)
        expected_output = "h.html"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
