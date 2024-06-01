# Solution to Exercise 7

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Calculate the sum of the integers in the list
total_sum = sum(numbers)

# Print the sum of the integers
print(total_sum)
