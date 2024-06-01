# Solution to Exercise 29

# Prompt the user to enter the size of the matrix (n)
n = int(input("Enter the size of the matrix (n): "))

# Initialize an n x n matrix with zeros
matrix = [[0 for _ in range(n)] for _ in range(n)]

# Define initial values for the spiral filling process
num = 1
left, right = 0, n - 1
top, bottom = 0, n - 1

# Fill the matrix in a spiral order
while left <= right and top <= bottom:
    # Fill the top row from left to right
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    # Fill the right column from top to bottom
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # Fill the bottom row from right to left
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    # Fill the left column from bottom to top
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

# Print the resulting spiral matrix
for row in matrix:
    print(" ".join(map(str, row)))
