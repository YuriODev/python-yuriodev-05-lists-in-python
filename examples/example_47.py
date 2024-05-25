# Read the input data
a, b, c = map(int, input("Enter the dimensions a, b, c: ").split())

# Create the 3D array with all elements set to 0
# - The outermost list has a length of a
# - Each inner list has a length of b
# - Each innermost list has a length of c
array_3d = [[[0 for _ in range(c)] for _ in range(b)] for _ in range(a)]

# Print the result
print(array_3d)