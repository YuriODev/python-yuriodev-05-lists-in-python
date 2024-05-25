# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Initialize variables to track the most frequent number
most_frequent = None  # Variable to store the most frequent number
max_count = 0  # Variable to store the count of the most frequent number
current_count = 0  # Variable to store the count of the current number being checked

# Sort the numbers in ascending order
sorted_numbers = sorted(numbers)

# Iterate through the sorted numbers to find the most frequent number
for i in range(len(sorted_numbers)):
    # If it's the first number or the same as the previous number, increment the count
    if i == 0 or sorted_numbers[i] == sorted_numbers[i - 1]:
        current_count += 1
    else:
        # If it's a new number, reset the count to 1
        current_count = 1

    # If the current count is greater than the max count, update the max count and most frequent number
    if current_count > max_count:
        max_count = current_count
        most_frequent = sorted_numbers[i]

# Print the most frequent number
print(most_frequent)
