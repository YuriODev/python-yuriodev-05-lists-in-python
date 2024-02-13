# Read the input numbers from the user
n = int(input("Enter the integer: "))
k = int(input("Enter the number of digits to cut off: "))

# Calculate the divisor
divisor = 10**k

# Calculate the result
result = n // divisor

# Print the result
print(result)
