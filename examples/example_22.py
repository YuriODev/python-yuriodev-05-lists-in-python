# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Find the largest element in the list
largest = max(numbers)

# Find the index of the first occurrence of the largest element
first_index = numbers.index(largest)

# Print the largest element and its first index
print(largest, first_index)
