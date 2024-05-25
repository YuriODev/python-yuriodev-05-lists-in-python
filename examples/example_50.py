# Read the input data
string_A = input("Enter the string A: ")  # Prompt the user to enter string A and store it in the variable string_A
substring_B = input("Enter the substring B: ")  # Prompt the user to enter substring B and store it in the variable substring_B

# Find all positions of the substring B in string A
positions = []  # Create an empty list to store the positions of substring B in string A
index = string_A.find(substring_B)  # Find the first occurrence of substring B in string A and store its index in the variable index
while index != -1:  # Continue the loop as long as substring B is found in string A
    positions.append(index + 1)  # Add the position of substring B (index + 1) to the positions list
    index = string_A.find(substring_B, index + 1)  # Find the next occurrence of substring B in string A starting from index + 1

# Print the result
if positions:  # Check if there are any positions found
    print(" ".join(map(str, positions)))  # Convert the positions list to a string and print it with spaces in between each position
else:
    print(-1)  # If no positions are found, print -1
