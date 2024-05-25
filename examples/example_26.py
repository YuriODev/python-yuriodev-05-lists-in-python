# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Count the number of equal pairs in the list
# - Convert the list to a set to remove duplicates
# - For each unique number in the set, count the number of occurrences in the original list
# - Divide the count by 2 to get the number of pairs
# - Sum up the counts of all numbers to get the total number of equal pairs
equal_pairs = sum(numbers.count(num) // 2 for num in set(numbers))

# Print the total number of equal pairs
print(equal_pairs)
