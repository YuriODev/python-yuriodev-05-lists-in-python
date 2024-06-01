# Solution to Exercise 18

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Find the minimum and maximum elements in the list
min_element = min(numbers)
max_element = max(numbers)

# Find the indices of the minimum and maximum elements
min_index = numbers.index(min_element)
max_index = numbers.index(max_element)

# Swap the minimum and maximum elements
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# Print the list after swapping
print(" ".join(map(str, numbers)))
