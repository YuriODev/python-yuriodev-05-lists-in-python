# Prompt the user to enter binary numbers separated by commas
input_numbers = input("Enter binary numbers separated by commas: ")

# Split the input string into a list of individual numbers
numbers = input_numbers.split(",")

# Create a new list called 'divisible_by_5' that will store binary numbers divisible by 5
# Iterate over each number in the 'numbers' list
# Convert each number from binary to decimal using the 'int' function with base 2
# Check if the decimal number is divisible by 5 using the modulo operator (%)
# If the number is divisible by 5, add it to the 'divisible_by_5' list using a list comprehension
divisible_by_5 = [num for num in numbers if int(num, 2) % 5 == 0]

# Convert the 'divisible_by_5' list back to a string, with each number separated by a comma
# Print the resulting string of binary numbers divisible by 5
print(",".join(divisible_by_5))

# Alternatively, you can use a traditional for loop to achieve the same result:

# Prompt the user to enter binary numbers separated by commas
input_numbers = input("Enter binary numbers separated by commas: ")

# Split the input string into a list of individual numbers
numbers = input_numbers.split(",")

# Create an empty list to store the binary numbers that are divisible by 5
divisible_by_5 = []

# Iterate over each number in the list
for num in numbers:

    # Convert the binary number to decimal using the int function with base 2
    decimal = int(num, 2)

    # Check if the decimal number is divisible by 5
    if decimal % 5 == 0:
        # If it is divisible by 5, add it to the list
        divisible_by_5.append(num)

# Join the divisible_by_5 list into a string with commas and print it
print(",".join(divisible_by_5))

# Alternatively, you can manually convert the binary numbers to decimal
# without using the int function:

# Prompt the user to enter binary numbers separated by commas
input_numbers = input("Enter binary numbers separated by commas: ")

# Split the input string into a list of individual numbers
numbers = input_numbers.split(",")

# Create an empty list to store numbers divisible by 5
divisible_by_5 = []

# Iterate over each number in the list
for num in numbers:
    # Initialize a variable to store the decimal value
    decimal = 0

    # Reverse the binary number string
    string_num = num[::-1]

    # Convert the binary number to decimal using manual conversion
    for i in range(len(string_num)):
        decimal += int(string_num[i]) * 2 ** i

    # Check if the decimal number is divisible by 5
    if decimal % 5 == 0:
        # If divisible by 5, add it to the list
        divisible_by_5.append(num)

# Join the divisible_by_5 list elements into a string separated by commas
result = ",".join(divisible_by_5)

# Print the final result
print(result)
