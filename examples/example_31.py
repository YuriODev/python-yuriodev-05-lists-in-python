# Read the input data
numbers = list(map(int, input("Enter three integers separated by spaces: ").split()))

# The input() function is used to prompt the user to enter three integers separated by spaces.
# The input is then split using the split() method, which splits the input string into a list of strings.
# The map() function is used to apply the int() function to each element of the list, converting them to integers.
# Finally, the list() function is used to convert the map object into a list and assign it to the variable 'numbers'.

# Sort the numbers
sorted_numbers = sorted(numbers)

# The sorted() function is used to sort the elements in the 'numbers' list in ascending order.
# The sorted list is then assigned to the variable 'sorted_numbers'.

# Find the median (the second element in the sorted list of three numbers)
median = sorted_numbers[1]

# The median is calculated by accessing the second element (index 1) in the 'sorted_numbers' list.
# Since the list is sorted in ascending order, the second element represents the median.

# Print the result
print(median)
