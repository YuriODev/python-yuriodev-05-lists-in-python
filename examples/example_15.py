# Read the input data
input_data = input("Enter a list of numbers separated by spaces: ")
stop_number = int(input("Enter the stop number: "))

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Iterate through the list and print even numbers until stop_number or zero is encountered
# Iterate through each number in the list
for number in numbers:
    # Check if the current number is equal to the stop number or zero
    if number == stop_number or number == 0:
        # If it is, exit the loop
        break
    # Check if the current number is even
    if number % 2 == 0:
        # If it is, print the number
        print(number)

