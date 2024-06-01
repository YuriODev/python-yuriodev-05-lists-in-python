# Solution to Exercise 10

# Prompt the user to enter a list of integers separated by spaces
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Prompt the user to enter an integer n
n = int(input("Enter an integer: "))

# Count the occurrences of n in the list
count = numbers.count(n)

# Print the count of occurrences of n
print(count)
