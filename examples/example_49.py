# Initialize the starting position
x, y = 0, 0

# Read the input data
while True:
    # Prompt the user to enter a movement command
    command = input("Enter movement command (or empty line to stop): ")

    # Check if the command is empty
    if not command:
        # If the command is empty, break out of the loop
        break

    # Split the command into direction and steps
    direction, steps = command.split()

    # Convert the steps to an integer
    steps = int(steps)

    # Check the direction and update the position accordingly
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

# Calculate the distance from the origin
distance = ((x ** 2) + (y ** 2)) ** 0.5

# Round up the distance to the nearest integer
distance = int(distance + 0.5)

# Print the result
print(distance)
