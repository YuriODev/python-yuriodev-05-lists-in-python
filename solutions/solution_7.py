# # Read the input
n = int(input())

# Extract the digits
d1 = n // 1000
d2 = (n % 1000) // 100
d3 = (n % 100) // 10
d4 = n % 10

# Calculate the sum of the digits
sum_of_digits = d1 + d2 + d3 + d4

# Print the sum of the digits
print(sum_of_digits)
