# Solution to Exercise 22

# Prompt the user to enter a binary number
input_data = input("")

# Convert the binary number to a list of digits
digits = list(map(int, input_data))

# Initialize the decimal number to 0
decimal_number = 0

# Loop through each digit in the binary number
for i in range(len(digits)):
    # Multiply the current digit by 2 raised to the power of its position
    decimal_number += digits[-i-1] * 2**i

# Print the decimal representation of the binary number
print(decimal_number)
