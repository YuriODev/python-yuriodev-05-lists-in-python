# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Set the initial output value to the first number in the list
output = numbers[0]

# Check if there are more than one elements in the list
if len(numbers) > 1:
    # Shift the elements to the right by moving the last element to the beginning
    shifted = [numbers[-1]] + numbers[:-1]
    # Convert the shifted list back to a string with space-separated numbers
    output = " ".join(map(str, shifted))

# Print the output
print(output)
