# Read the input data
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Create a list to store the counts of each number
counts = [0] * (max(numbers) + 1)

# Count the occurrences of each number
for number in numbers:
    counts[number] += 1

# Find numbers that occur more than once and sort them
# -- enumerate() returns the index and the value of each element
# -- list comprehension is used to filter the numbers with count > 1
# extract the index (number) and store it in the list of duplicates
duplicates = [number for number, count in enumerate(counts) if count > 1]

# Print the result
print(" ".join(map(str, duplicates)))
