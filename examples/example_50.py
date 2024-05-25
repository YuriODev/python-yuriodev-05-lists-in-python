# Read the input data
n, k = map(int, input("Enter the number of pins and throws: ").split())

# Initialize the pins as standing (I)
pins = ['I'] * n

# Process each throw
for _ in range(k):
    # Read the range of pins to be knocked down
    m, h = map(int, input("Enter the range m to h: ").split())

    # Update the status of the knocked down pins
    for i in range(m-1, h):
        pins[i] = '.'

# Print the result
print("".join(pins))
