# Read the input
a = int(input())
b = int(input())

# Calculate the maximum value
max_value = (a + b + abs(a - b)) // 2

# Alternative solution
max_value = a * (a > b) + b * (b >= a)

# Print the maximum value
print(max_value)
