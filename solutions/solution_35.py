# Solution to Exercise 35

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Initialize pointers for the left and right parts of the list
left = 0

# Move non-zero elements to the left side of the list
for right in range(len(numbers)):
    # Move non-zero elements to the left side of the list
    for right in range(len(numbers)):

        # Check if the current element is non-zero
        if numbers[right] != 0:

            # Swap the current element with the element at the left pointer
            numbers[left], numbers[right] = numbers[right], numbers[left]

            # Increment the left pointer to move to the next position
            left += 1

# Print the resulting list with all non-zero elements on the left and zeros on the right
print(" ".join(map(str, numbers)))
