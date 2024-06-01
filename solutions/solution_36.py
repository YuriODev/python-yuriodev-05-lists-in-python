# Solution to Exercise 36

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Prompt the user to enter the number to search for
x = int(input("Enter the number to search for: "))

# Find and print all positions of the number in the list
positions = [str(i + 1) for i, num in enumerate(numbers) if num == x]
if positions:
    print(" ".join(positions))
else:
    print("None")
