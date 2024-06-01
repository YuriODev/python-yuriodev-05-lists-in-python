# Solution to Exercise 9

# Prompt the user to enter a sequence of numbers separated by commas
input_data = input("Enter a sequence of numbers separated by commas: ")

# Convert the input string into a list of integers
numbers_list = list(map(int, input_data.split(',')))

# Convert the input string into a tuple of integers
numbers_tuple = tuple(numbers_list)

# Print the list and tuple
print(numbers_list)
print(numbers_tuple)
