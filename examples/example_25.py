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

# Alternative solution

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Find the minimum value in the list
min_value = min(numbers)

# Find the maximum value in the list
max_value = max(numbers)

# Iterate over the indices of the numbers list
for i in range(len(numbers)):
    # If the current number is equal to the minimum value, replace it with the maximum value
    if numbers[i] == min_value:
        numbers[i] = max_value
    # If the current number is equal to the maximum value, replace it with the minimum value
    elif numbers[i] == max_value:
        numbers[i] = min_value

# Convert the modified numbers list back to a string and join the elements with spaces
result = " ".join(map(str, numbers))

# Print the modified numbers string
print(result)
