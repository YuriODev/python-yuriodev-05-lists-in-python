# Solution to Exercise 12

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(str, input_data.split()))

# Concatenate the integers to form a single integer
single_integer = ''.join(numbers)

# Print the single integer
print(single_integer)
