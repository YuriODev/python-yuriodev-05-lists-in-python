# Read the input data
a, b = map(int, input("Enter two integers a and b: ").split())

# Generate the 2D array defined by the formula a[i][j] = i * j
array = [[i * j for j in range(b)] for i in range(a)]

# Print the result
print(array)