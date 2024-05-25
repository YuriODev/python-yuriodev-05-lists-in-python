# Read the input data
n = int(input("Enter a non-negative integer: "))

# Generate the sequence
sequence = []

# Initialize the current_number variable to 1
current_number = 1

# Continue the loop until the length of the sequence is less than n
while len(sequence) < n:
    # Extend the sequence by adding current_number repeated current_number times
    sequence.extend([current_number] * current_number)

    # Increment the current_number by 1 for the next iteration
    current_number += 1

# Trim the sequence to the desired length (n) and convert it to a string with 
# space-separated elements
# Then, print the sequence
print(" ".join(map(str, sequence[:n])))
