# Solution to Exercise 21

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Prompt the user to enter two integers k and c
k = int(input("Enter the position index (k): "))
c = int(input("Enter the value to insert (c): "))

# Insert the value c at position k, shifting elements to the right
# (using slices)
numbers = numbers[:k] + [c] + numbers[k:]

# Print the list after insertion
print(" ".join(map(str, numbers)))
