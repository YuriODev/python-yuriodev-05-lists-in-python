# Read the input data
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Find the elements greater than the previous one
# The list comprehension iterates over the indices of the list
# and selects the elements that are greater than the previous one
# The range starts from 1 to avoid comparing the first element with a non-existent previous element
# The condition checks if the current element is greater than the previous one
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]

# Print the result
print(" ".join(map(str, result)))
