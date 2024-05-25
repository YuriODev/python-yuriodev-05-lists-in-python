# Prompt the user to enter heights separated by spaces
input_heights = input("Enter heights separated by spaces: ")

# Split the input string into a list of strings, then convert each string to an integer
heights = list(map(int, input_heights.split()))

# Prompt the user to enter the height of the new student and convert it to an integer
new_height = int(input("Enter the height of the new student: "))

# Find the position for the new student
position = 1
for height in heights:
    # Compare the new height with each height in the list
    if new_height >= height:
        # If the new height is greater than or equal to the current height, stop the loop
        break
    # If the new height is smaller than the current height, increment the position
    position += 1

# Print the position of the new student
print(position)
