# Solution to Exercise 31

# Prompt the user to enter a list of integers separated by spaces
input_data = input("")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Initialize an empty list to store the sums of neighbors
result = []

# If there is only one number, return it as the result
if len(numbers) == 1:
    result.append(numbers[0])
else:
    # Calculate the sum of neighbors for each element
    # Iterate over each element in the numbers list
    for i in range(len(numbers)):
        # Get the left neighbor of the current element
        left_neighbor = numbers[i - 1]

        # Get the right neighbor of the current element
        right_neighbor = numbers[(i + 1) % len(numbers)]

        # Calculate the sum of the left and right neighbors
        neighbor_sum = left_neighbor + right_neighbor

        # Add the sum to the result list
        result.append(neighbor_sum)

# Print the resulting list of sums
print(" ".join(map(str, result)))
