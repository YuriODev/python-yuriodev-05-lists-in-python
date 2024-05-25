# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Remove every third element until the list is empty
index = 2  # Initialize the index variable to 2, representing the third element in the list

while len(numbers) > 0:  # Continue the loop until the list is empty
    print(numbers)  # Print the current state of the list

    if len(numbers) > index:  # Check if the index is within the bounds of the list
        numbers.pop(index)  # Remove the element at the current index
        index += 2  # Increment the index by 2 to skip the next element
    else:
        index = (index - len(numbers)) % 3  # Calculate the new index value based on the remaining elements in the list
        if index == 0:  # If the new index is 0, set it back to 2 to maintain the pattern
            index = 2

# The modified code removes every third element from the list until the list becomes empty.
# The final state of the list is printed.

# Print the final empty list
print(numbers)
