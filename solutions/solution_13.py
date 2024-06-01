# Solution to Exercise 13

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Calculate the arithmetic mean of the elements
arithmetic_mean = sum(numbers) / len(numbers)

# Print the arithmetic mean rounded to two decimal places
print(f"{arithmetic_mean:.2f}")
