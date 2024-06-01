# Solution to Exercise 3

# Prompt the user to enter a list of numbers separated by spaces
input_data = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = list(map(int, input_data.split()))

# Create an empty list to store even numbers
even_numbers = []

# Iterate through the list of numbers
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        # Append the even number to the even_numbers list
        even_numbers.append(number)

# Solution using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]


# Print the even numbers separated by spaces
print(" ".join(map(str, even_numbers)))
