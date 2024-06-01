# Solution to Exercise 25

# Prompt the user to enter an odd natural number
n = int(input("Enter an odd natural number: "))

# Initialize a 2D array of size n x n with the symbol '.'
snowflake = [['.' for _ in range(n)] for _ in range(n)]

# Fill the middle row, middle column, and diagonals with the symbol '*'
for i in range(n):
    snowflake[i][i] = '*'
    snowflake[i][n - i - 1] = '*'
    snowflake[i][n // 2] = '*'
    snowflake[n // 2][i] = '*'

# Print the snowflake pattern with symbols separated by spaces
for row in snowflake:
    print(" ".join(row))
