# Prompt the user to enter numbers separated by spaces
input_numbers = input("Enter numbers separated by spaces: ")

# Split the input string into a list of individual numbers and convert them to integers
numbers = list(map(int, input_numbers.split()))

# Output the index and value of each element in the numbers list
for index, value in enumerate(numbers): # Using the enumerate function to get the index and value
    print(index, value)

# Alternatively, you can use a traditional for loop with range(len(numbers))

# Output the index and value of each element
for i in range(len(numbers)):
    print(i, numbers[i])
