# Solution to Exercise 16

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Create a list to store elements that appear only once
unique_elements = []

# Iterate through the list of numbers
for number in numbers:
    # Check if the number appears only once in the list
    if numbers.count(number) == 1:
        # Add the number to the unique_elements list
        unique_elements.append(number)

# Print the unique elements separated by spaces
print(" ".join(map(str, unique_elements)))
