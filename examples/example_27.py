# Prompt user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Solution 1 - Swap adjacent elements in pairs
# The list comprehension iterates over the indices of the numbers list
# If the index is even, the next element is swapped with the current element
# If the index is odd, the previous element is swapped with the current element
# The swapped elements are stored in the swapped list
swapped = [numbers[i + 1] if i % 2 == 0 else numbers[i - 1] for i in range(len(numbers))]

# Solution 2 - Using for loop
# Initialize an empty list to store the swapped elements
# Iterate over the indices of the numbers list in steps of 2
# Swap the adjacent elements and add them to the swapped list
swapped = []
for i in range(0, len(numbers), 2):
    swapped.extend([numbers[i + 1], numbers[i]])

# Print the result
print(" ".join(map(str, swapped)))
