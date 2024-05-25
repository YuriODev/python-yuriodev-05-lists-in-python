# Input data
input_numbers = input("Enter numbers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_numbers.split()))

# Find the indices of the minimum and maximum elements
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Swap the minimum and maximum elements
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# Print the result
print(" ".join(map(str, numbers)))
