# Prompt the user to enter a sequence of integers
input_sequence = input("Enter a sequence of integers: ")

# Split the input sequence by spaces and convert each element to an integer
numbers = list(map(int, input_sequence.split()))

# Check if the length of the numbers list is greater than or equal to 2
if len(numbers) >= 2:
    # Extract the last two elements from the numbers list
    last_two = numbers[-2:]

    # Remove the last two elements from the numbers list
    remaining_numbers = numbers[:-2]

    # Create a new list by concatenating the last two elements at the beginning of the remaining_numbers list
    new_order = last_two + remaining_numbers

    # Convert each element of the new_order list to a string and join them with a space separator
    print(" ".join(map(str, new_order)))