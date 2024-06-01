# Solution to Exercise 8

# Prompt the user to enter a floating-point number
input_data = input("Enter a floating-point number: ")

# Split the input data into integer and fractional parts using the decimal point as the separator
integer_part, fractional_part = input_data.split('.')

# Print the integer part and the fractional part separately
print(integer_part, fractional_part)
