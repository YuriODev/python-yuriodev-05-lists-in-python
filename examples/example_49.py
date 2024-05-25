# Read the input data
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
k = int(input("Enter the value of k: "))  # Prompt the user to enter the value of k

# Normalize k to be within the range of the list length
n = len(numbers)  # Get the length of the numbers list
k = k % n  # Calculate the remainder of k divided by n to ensure k is within the range of the list length

# Perform the cyclic shift
if k > 0:  # If k is positive
    numbers = numbers[-k:] + numbers[:-k]  # Perform a right cyclic shift by slicing the list
else:  # If k is negative or zero
    k = -k  # Convert k to positive
    numbers = numbers[k:] + numbers[:k]  # Perform a left cyclic shift by slicing the list

# Print the result
print(" ".join(map(str, numbers)))  # Convert the numbers list to a string and print it with spaces in between
