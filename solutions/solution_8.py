# Read the input
a = int(input())
b = int(input())
c = int(input())

# Calculate the minimum, middle, and maximum values
min_value = a * (a <= b and a <= c) + b * (b < a or b < c) + c * (c < a and c < b)
max_value = a * (a >= b and a >= c) + b * (b > a or b > c) + c * (c > a and c > b)
mid_value = a + b + c - min_value - max_value

# Print the sorted numbers
print(min_value)
print(mid_value)
print(max_value)
