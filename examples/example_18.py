# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Prompt the user to enter an integer value for n
n = int(input("Enter an integer n: "))

# Check if n exceeds all elements in the list by comparing it to the maximum value in the list
exceeds_all = n > max(numbers)

# Print the result indicating whether n exceeds all elements in the list
print(exceeds_all)
