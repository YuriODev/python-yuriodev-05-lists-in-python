# Solution to Exercise 5

# Prompt the user to enter a list of numbers separated by spaces
input_data = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Create an empty set to store unique elements
unique_elements = set()

# Iterate through the list of numbers
for number in numbers:
    # Add each number to the set of unique elements
    unique_elements.add(number)

# Solution using set comprehension
unique_elements = set(numbers)

# Print the count of unique elements
print(len(unique_elements))
