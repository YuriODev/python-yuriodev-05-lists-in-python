import unittest
from .enhanced_string_io import StringIOWithWriteLn as StringIO


class CustomTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, stream=StringIO(), **kwargs)

    def run(self, test):
        result = super().run(test)
        self.report_test_results(result)
        return result

    # def report_test_results(self, test_results):
    #     total_tests = test_results.testsRun
    #     failed_tests = len(test_results.failures) + len(test_results.errors)
    #     passed_tests = total_tests - failed_tests
    #     passed_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

    #     if failed_tests > 0:
    #         print(f"\x1b[6;30;41m Tests passed: {passed_tests}/{total_tests} ({passed_percentage:.2f}%) \x1b[0m")
    #         # Process each failure individually
    #         for failure in test_results.failures + test_results.errors:
    #             test_case, failure_message = failure
    #             # Check for specific types of failures
    #             if "Loop Usage Error" in failure_message:
    #                 # Custom handling for loop usage errors
    #                 self.print_loop_usage_error(failure_message)
    #             elif "Failed test:" in failure_message:
    #                 # Custom handling for other failed tests
    #                 self.print_failed_test_error(failure_message)
    #             else:
    #                 # Default error message handling
    #                 print(failure_message)
    #     else:
    #         print("\x1b[6;30;42m Success! Your code works as intended. \x1b[0m")

    # def print_loop_usage_error(self, failure_message):
    #     # Implement custom printing logic for loop usage errors
    #     print(f"\x1b[6;30;43m{failure_message}\x1b[0m")

    # def print_failed_test_error(self, failure_message):
    #     # Implement custom printing logic for failed test errors
    #     print(f"\x1b[6;30;41m{failure_message}\x1b[0m")
