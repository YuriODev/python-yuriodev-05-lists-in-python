# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Prompt the user to enter an integer n
n = int(input("Enter an integer n: "))

# Initialize a boolean variable to track if n exceeds all elements in the list
exceeds_all = True

# Iterate through each number in the list
for num in numbers:
    # Check if n is less than or equal to the current number
    if n <= num:
        # If n is less than or equal to any number, set exceeds_all to False and break out of the loop
        exceeds_all = False
        break

# Print the value of exceeds_all, which indicates if n exceeds all elements in the list
print(exceeds_all)


# Alternatively, you can use the all() function with a generator expression

# Check if n exceeds all elements in the list using the all() function with a generator expression
exceeds_all = all(n > num for num in numbers)

# Print the result indicating whether n exceeds all elements in the list
print(exceeds_all)

# Check if n exceeds all elements in the list by comparing it to the maximum value in the list
exceeds_all = n > max(numbers)

# Print the result indicating whether n exceeds all elements in the list
print(exceeds_all)
