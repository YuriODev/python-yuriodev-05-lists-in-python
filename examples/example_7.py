# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Create a new list to store unique elements in order
# Iterate over each number in the 'numbers' list
# Check if the count of the current number in the 'numbers' list is equal to 1
# If it is, add the number to the 'unique_list'
unique_list = [num for num in numbers if numbers.count(num) == 1]

# Convert the elements in the 'unique_list' to strings and join them with spaces
# Print the resulting string of unique elements
print(" ".join(map(str, unique_list)))