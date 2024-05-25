# Read the input data
n, m = map(int, input("Enter the dimensions n and m: ").split())

# Create the chessboard pattern
chessboard = []
for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:  # Check if the sum of i and j is even
            row.append('.')  # Add a '.' to the row if the sum is even
        else:
            row.append('*')  # Add a '*' to the row if the sum is odd
    chessboard.append(" ".join(row))  # Join the row elements with a space and add it to the chessboard list

# Print the chessboard pattern
for row in chessboard:
    print(row)  # Print each row of the chessboard pattern
