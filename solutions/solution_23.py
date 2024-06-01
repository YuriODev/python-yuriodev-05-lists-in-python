# Solution to Exercise 23

# Prompt the user to enter a string of digits separated by spaces
input_data = input("Enter a string of digits separated by spaces: ")

# Convert the input string into a list of digits
digits = input_data.split()

# Create a new list with elements sorted in reverse order
reversed_digits = sorted(digits, reverse=True)

# Concatenate the elements of the reversed list to form a number
result = ''.join(reversed_digits)

# Print the resulting number
print(result)
