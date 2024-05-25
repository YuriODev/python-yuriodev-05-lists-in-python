# Read the input data
a, b, c = map(int, input("Enter the dimensions a, b, c: ").split())

# Create the 3D array with all elements set to 0
# -- the outermost list comprehension creates the 3D array
# -- the middle list comprehension creates the 2D arrays
# -- the innermost list comprehension creates the 1D arrays
# -- the value 0 is used to initialize all elements
array_3d = [[[0 for _ in range(c)] for _ in range(b)] for _ in range(a)]

# Print the result
print(array_3d)
