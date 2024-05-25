# Read the input data
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Sort the list
numbers.sort()

# Count the number of non-repeating elements
# Initialize a variable to keep track of the number of unique elements
unique_count = 1

# Iterate through the list starting from the second element
for i in range(1, len(numbers)):
    # Check if the current element is different from the previous element
    if numbers[i] != numbers[i-1]:
        # If it is different, increment the unique_count variable
        unique_count += 1

# At this point, the unique_count variable will hold the number of
# non-repeating elements in the list

# Print the result
print(unique_count)
