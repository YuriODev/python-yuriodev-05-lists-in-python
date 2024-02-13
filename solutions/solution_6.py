# Read the input
a = int(input())
b = int(input())

# Check if a is divisible by b
divisible = "YES" * (a % b == 0) or "NO"

# Print the result
print(divisible)
