# Read the input data
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Find the two smallest elements

# Check if the list has less than 2 elements
if len(numbers) < 2:
    print("Not enough elements to find two smallest.")
else:
    # Initialize the two smallest variables with infinity
    min1, min2 = float('inf'), float('inf')

    # Iterate through each number in the list
    for num in numbers:
        # If the current number is smaller than the current smallest number,
        # update the second smallest number and update the smallest number
        if num < min1:
            min2 = min1
            min1 = num
        # If the current number is larger than the smallest number but smaller
        # than the second smallest number, update the second smallest number
        elif num < min2:
            min2 = num

    # Print the two smallest numbers
    print(min1, min2)
