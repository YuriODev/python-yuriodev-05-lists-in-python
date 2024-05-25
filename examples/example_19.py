# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Find the smallest number
min_number = min(numbers)

# Print the result
print(min_number)
