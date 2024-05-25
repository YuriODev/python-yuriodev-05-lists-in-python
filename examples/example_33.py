# Read the input data
input_data1 = input("Enter the first list of integers separated by spaces and commas: ")
input_data2 = input("Enter the second list of integers separated by spaces and commas: ")

# Convert the input data to sets of integers
# Remove commas and split the input strings into a list of integers
# Convert the list of integers to a set
set1 = set(map(int, input_data1.replace(',', '').split()))
set2 = set(map(int, input_data2.replace(',', '').split()))

# Find the intersection of the two sets
common_elements = sorted(set1.intersection(set2))

# Alternative solution using list comprehension
# Find the common elements between the two sets
# Sort the common elements in ascending order
common_elements = sorted([num for num in set1 if num in set2])

# Print the result
print(" ".join(map(str, common_elements)))
