# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of strings and convert each string to an integer
numbers = list(map(int, input_numbers.split()))

# Find and print adjacent elements with the same sign
# Iterate over the range of indices in the numbers list, excluding the last index
for i in range(len(numbers) - 1):
    # Check if the product of the current number and the next number is greater than 0
    if numbers[i] * numbers[i + 1] > 0:
        # If the product is greater than 0, print the current number and the next number
        print(numbers[i], numbers[i + 1])
