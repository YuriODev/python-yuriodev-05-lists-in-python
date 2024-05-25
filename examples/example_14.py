# Read the input data
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Find the smallest number
min_number = min(numbers)

# Find the largest number
max_number = max(numbers)

# Find the number of elements
count_numbers = len(numbers)

# Find the average value
average_value = sum(numbers) / count_numbers

# Print the results
print(min_number)
print(max_number)
print(count_numbers)
print(average_value)
