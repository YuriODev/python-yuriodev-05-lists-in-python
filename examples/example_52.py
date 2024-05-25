# Read the input data
input_data = input("Enter a sequence of integer lists separated by commas: ")

# Convert the input data into a list of lists
list_of_lists = [list(map(int, item.split())) for item in input_data.split(',')]

# Print the initial list of lists
print(list_of_lists)

# Sort the list of lists by the second element of each sublist
sorted_list_of_lists = sorted(list_of_lists, key=lambda x: x[1])

# Print the sorted list of lists
print(sorted_list_of_lists)

# Alternative solution using pure Python
# Read the input data
input_data = input("Enter a sequence of integer lists separated by commas: ")

# Split the input data into a list of lists
list_of_lists = [item.split() for item in input_data.split(',')]

# Convert the strings to integers
for i in range(len(list_of_lists)):
    list_of_lists[i] = [int(x) for x in list_of_lists[i]]

# Print the initial list of lists
print(list_of_lists)

# Sort the list of lists by the second element of each sublist using sorting algorithm (bubble sort)
n = len(list_of_lists)

# Iterate over the range of numbers from 0 to n-1
for i in range(n):
    # Iterate over the range of numbers from 0 to n-i-1
    # The range decreases with each iteration to avoid unnecessary comparisons
    for j in range(0, n-i-1):
        # Compare the second element of the current sublist with the second element of the next sublist
        if list_of_lists[j][1] > list_of_lists[j+1][1]:
            # Swap the positions of the current sublist and the next sublist if the second element of the current sublist is greater
            list_of_lists[j], list_of_lists[j+1] = list_of_lists[j+1], list_of_lists[j]

# Print the sorted list of lists
print(list_of_lists)
