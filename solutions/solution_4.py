# Solution to Exercise 4

# Prompt the user to enter a list of numbers separated by commas without spaces
input_data = input("Enter a list of numbers separated by commas without spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split(',')))

# Create an empty list to store elements with odd indices
odd_index_elements = []

# Iterate through the list of numbers using index
for i in range(len(numbers)):
    # Check if the index is odd
    if i % 2 != 0:
        # Append the element with an odd index to the odd_index_elements list
        odd_index_elements.append(numbers[i])

# Solution using list comprehension
odd_index_elements = [numbers[i] for i in range(len(numbers)) if i % 2 != 0]

# Print the elements with odd indices separated by commas without spaces
print(",".join(map(str, odd_index_elements)))
