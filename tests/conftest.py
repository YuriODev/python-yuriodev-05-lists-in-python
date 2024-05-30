def pytest_sessionfinish(session, exitstatus):
    """Prints a custom success message at the end of a successful test session."""
    if exitstatus == 0:  # exitstatus 0 indicates all tests passed
        print("\x1b[6;30;42m Success! Your code works as intended. \x1b[0m")


def pytest_exception_interact(node, call, report):
    if report.failed:
        # Check if the custom message is in the failure's long representation ('longrepr')
        if "Failed test:" in str(report.longrepr):
            # Isolate the table part of the message
            table_start_index = str(report.longrepr).find("Failed test:")
            custom_table = str(report.longrepr)[table_start_index-25:]

            # Replace the long representation with the custom table
            report.longrepr = custom_table
