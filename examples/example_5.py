# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Prompt the user to enter the threshold number n
n = int(input("Enter the threshold number n: "))

# Split the input_numbers string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Filter the numbers list to only include elements that are less than n
filtered_numbers = [num for num in numbers if num < n]

# Convert the filtered_numbers list to a string and join the elements with spaces
result = " ".join(map(str, filtered_numbers))

# Print the result
print(result)
