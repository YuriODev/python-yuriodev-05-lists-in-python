# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Create a list of positive numbers
positive_numbers = [num for num in numbers if num > 0]

# Print the result
print(positive_numbers)
