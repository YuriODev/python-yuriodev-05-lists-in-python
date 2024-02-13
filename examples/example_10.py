# Read the input number from the user
n = int(input("Enter a three-digit number: "))

# Extract the hundreds, tens, and units digits
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10

# Construct the reversed number
reversed_n = units * 100 + tens * 10 + hundreds

# Print the result
print(reversed_n)
