# Solution to Exercise 32

# Prompt the user to enter the number of lines
n = int(input("Enter the number of lines: "))

# Initialize an empty list to store the lines
lines = []

# Read each line and store it in the list
for _ in range(n):
    lines.append(input("Enter a line of text: "))

# Find the maximum length of the lines
max_length = max(len(line) for line in lines)

# Find and print the line numbers of the longest lines
for i, line in enumerate(lines):
    if len(line) == max_length:
        print(i + 1)
