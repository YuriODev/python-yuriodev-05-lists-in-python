# Solution to Exercise 6

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Create an empty list to store elements greater than their neighbors
greater_than_neighbors = []

# Iterate through the list of numbers starting from the second element
# and ending at the second last element
for i in range(1, len(numbers) - 1):
    # Check if the current element is greater than both its neighbors
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        # Add the current element to the greater_than_neighbors list
        greater_than_neighbors.append(numbers[i])

# Print the count of elements greater than their neighbors
print(len(greater_than_neighbors))
