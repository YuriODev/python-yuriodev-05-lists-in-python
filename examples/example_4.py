# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string by spaces and convert each element to an integer
numbers = list(map(int, input_numbers.split()))

# Select and print elements with even indices
print(" ".join(map(str, numbers[::2])))
