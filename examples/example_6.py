# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Count the number of positive elements in the list using a generator expression
positive_count = sum(1 for num in numbers if num > 0)

# Print the count of positive elements
print(positive_count)