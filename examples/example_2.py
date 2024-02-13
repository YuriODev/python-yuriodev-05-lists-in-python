# Read the input number from the user
number = int(input("Enter a three-digit number: "))

# Extract each digit
hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

# Calculate the sum of the digits
sum_of_digits = hundreds + tens + ones

# Print the result using f-string
print(f"The sum of the digits of {number} is {sum_of_digits}")
