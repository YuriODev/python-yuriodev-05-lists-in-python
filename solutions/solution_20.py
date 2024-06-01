# Solution to Exercise 20

# Prompt the user to enter a string of text
text = input("Enter a string of text: ")

# Prompt the user to enter an integer representing the word's position
position = int(input("Enter the word's position: "))

# Split the text into words
words = text.split()

# Find the word at the specified position (1-based index) and get its first letter
first_letter = words[position - 1][0]

# Print the first letter of the word at the specified position
print(first_letter)
