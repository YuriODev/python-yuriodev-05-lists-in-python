numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
k = int(input("Enter the index to remove: "))

# Remove the element at index k and shift the remaining elements
for i in range(k, len(numbers) - 1):
    numbers[i] = numbers[i + 1]

# Remove the last element since it's now duplicated
numbers.pop()

# Print the result
print(" ".join(map(str, numbers)))
