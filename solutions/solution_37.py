# Solution to Exercise 37

# Prompt the user to enter a run-length encoded string
encoded_string = input("Enter a run-length encoded string: ")

# Initialize an empty list to store the decoded characters
decoded_string = []

# Iterate through the encoded string and decode it
i = 0
while i < len(encoded_string):
    # Check if the current character is a digit
    if encoded_string[i].isdigit():
        # Get the full number (in case of multi-digit numbers)
        num_str = ''
        while i < len(encoded_string) and encoded_string[i].isdigit():
            # Add the current digit to the number string
            num_str += encoded_string[i]
            # Move to the next character in the encoded string
            i += 1
        # Convert the number string to an integer
        num = int(num_str)
        # Append the character num times to the decoded string
        decoded_string.append(encoded_string[i] * num)
    else:
        # Append the character once if no number precedes it
        decoded_string.append(encoded_string[i])
    i += 1

# Print the decoded string
print("".join(decoded_string))
