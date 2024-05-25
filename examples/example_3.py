# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Print the list in reverse order without altering the original list
print(" ".join(map(str, numbers[::-1])))
