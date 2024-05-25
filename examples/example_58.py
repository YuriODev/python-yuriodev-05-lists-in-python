# Read the input data
number = input("Enter an integer number: ")

# Convert the integer to a list of digits
digits = [int(d) for d in number]

# Find the maximum number after removing one digit
max_number = 0
for i in range(len(digits)):
    # Create a temporary list by removing the i-th digit from the original list
    temp_digits = digits[:i] + digits[i+1:]

    # Convert the temporary list of digits back to an integer
    temp_number = int(''.join(map(str, temp_digits)))

    # Check if the temporary number is greater than the current maximum number
    if temp_number > max_number:
        # Update the maximum number if the temporary number is greater
        max_number = temp_number

# Print the result
print(max_number)
