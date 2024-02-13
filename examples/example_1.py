# Read the input number from the user
number = int(input("Enter a natural number: "))

# Get ten place digit using integer division and modulo
tens_place = (number // 10) % 10

# Print the result using f-string
print(f"The tens place digit of {number} is {tens_place}")