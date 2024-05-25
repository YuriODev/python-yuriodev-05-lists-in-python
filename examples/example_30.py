# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Calculate the squares of the elements in the numbers list using a list comprehension
squares = [num ** 2 for num in numbers]

# Convert the squares list to a string and join the elements with a space separator
# Then print the resulting string
print(" ".join(map(str, squares)))
