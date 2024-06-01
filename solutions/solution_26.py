# Solution to Exercise 26

# Prompt the user to enter a sequence of integers separated by spaces
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Sort even numbers in descending order and odd numbers in ascending order
even_numbers.sort(reverse=True)
odd_numbers.sort()

# Concatenate the even and odd numbers
result = even_numbers + odd_numbers

# Print the resulting list
print(" ".join(map(str, result)))
