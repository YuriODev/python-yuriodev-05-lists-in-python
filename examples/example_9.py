input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Output the index and value of each element
for i in range(len(numbers)):
    print(i, numbers[i])
