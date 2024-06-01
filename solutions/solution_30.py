# Solution to Exercise 30

# Prompt the user to enter the shift value for the Caesar cipher
shift = int(input("Enter the shift value: "))

# Prompt the user to enter the string of emojis to be encrypted
emoji_string = input("Enter the string of emojis: ")

# Define the range of the Unicode code points for the emojis
# start = 0x1F600
# end = 0x1F64F
start = 128512
end = 128591
num_emojis = end - start + 1

# Encrypt the emoji string using the Caesar cipher with cyclic shift
# Initialize an empty list to store the encrypted emojis
encrypted_emojis = []

# Iterate over each emoji in the input string
for emoji in emoji_string:
    # Get the Unicode code point of the emoji
    code_point = ord(emoji)

    # Apply the Caesar cipher encryption with the given shift value
    new_code_point = start + (code_point - start + shift) % num_emojis

    # Convert the new code point back to a character and append it to the encrypted_emojis list
    encrypted_emojis.append(chr(new_code_point))

# Print the encrypted emoji string
print("".join(encrypted_emojis))
