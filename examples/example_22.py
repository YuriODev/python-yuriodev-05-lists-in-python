# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of strings using spaces as separators,
# and then convert each string element into an integer using the map() function
numbers = list(map(int, input_numbers.split()))

# Create a set from the list of numbers, which removes duplicates,
# then sort the set in ascending order and convert it back to a list
# Finally, access the second element (index 1) of the sorted list
second_smallest = sorted(set(numbers))[1]

# Print the second smallest element
print(second_smallest)
