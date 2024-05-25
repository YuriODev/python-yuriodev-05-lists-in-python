# Read the input data
roman = input("Enter a Roman numeral: ")

# Define the values of Roman numerals
roman_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
decimal_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

# Initialize the index for roman_values and decimal_values
i = 0
decimal = 0
pos = 0

# Convert Roman numeral to decimal
while pos < len(roman):
    # Check if the current position and the next position form a valid Roman numeral
    if pos + 1 < len(roman) and roman[pos:pos+2] in roman_values:
        # Add the decimal value of the Roman numeral to the total
        decimal += decimal_values[roman_values.index(roman[pos:pos+2])]
        # Move the position by 2 to skip the next character
        pos += 2
    else:
        # Add the decimal value of the current Roman numeral to the total
        decimal += decimal_values[roman_values.index(roman[pos])]
        # Move the position by 1
        pos += 1

# Print the result
print(decimal)
