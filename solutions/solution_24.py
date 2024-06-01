# Solution to Exercise 24

# Prompt the user to enter a sequence of integers separated by spaces
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Separate the positive and negative numbers
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

# Sort positive numbers in descending order and negative numbers in descending order
positive_numbers.sort(reverse=True)
negative_numbers.sort(reverse=True)

# Concatenate the positive and negative numbers
result = positive_numbers + negative_numbers

# Print the resulting list
print(" ".join(map(str, result)))
