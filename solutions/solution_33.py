# Solution to Exercise 33

# Prompt the user to enter an integer
n = input("Enter an integer: ")

# Initialize a variable to store the maximum possible number
max_number = 0

# Iterate over each digit and remove it to find the maximum number
for i in range(len(n)):
    # Extract a possible number by removing the current digit at index i
    possible_number = int(n[:i] + n[i + 1:])

    # Check if the possible number is greater than the current maximum number
    if possible_number > max_number:
        # If it is, update the maximum number with the possible number
        max_number = possible_number

# Print the maximum possible number
print(max_number)
