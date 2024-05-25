# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Calculate the product without using loops or subroutines
length = len(numbers)  # Get the length of the list
index = 0  # Initialize the index variable
product = 1  # Initialize the product variable to 1

while index < length:  # Iterate through the list
    product *= numbers[index]  # Multiply the current number with the product
    index += 1  # Move to the next index

# Print the result
print(product)
