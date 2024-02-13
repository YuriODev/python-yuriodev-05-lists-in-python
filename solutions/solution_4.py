# Read the input
n = int(input())

# Extract the digits
d1 = n // 1000
d2 = (n % 1000) // 100
d3 = (n % 100) // 10
d4 = n % 10

# # SOLUTION 1

# # Calculate the result
# result = (d1 == d4) * (d2 == d3)

# # Print the result
# print(result)

# SOLUTION 2

# Calculate the difference
difference = abs((d1 - d4) + (d2 - d3))

# Print the result
print(max(1 - difference, 0))