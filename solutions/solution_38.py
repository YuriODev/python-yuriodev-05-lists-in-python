# Solution to Exercise 38

# Prompt the user to enter a four-digit positive decimal number
number = input("")

# Convert the input number to a list of its digits
digits = list(number)

# Generate all permutations manually and filter out invalid ones
permutations = []

# Iterate over each digit in the input number
for i in range(len(digits)):

    # Iterate over each digit again to form the second digit of the permutation
    for j in range(len(digits)):
        # Skip if the second digit is the same as the first digit
        if j == i:
            continue

        # Iterate over each digit again to form the third digit of the permutation
        for k in range(len(digits)):
            # Skip if the third digit is the same as the first or second digit
            if k == i or k == j:
                continue
            # Iterate over each digit again to form the fourth digit of the permutation

            for l in range(len(digits)):
                # Skip if the fourth digit is the same as any of the previous three digits
                if l == i or l == j or l == k:
                    continue

                # Concatenate the four digits to form a permutation
                perm = digits[i] + digits[j] + digits[k] + digits[l]

                # Convert the permutation to an integer
                perm_number = int(perm)

                # Check if the permutation is a four-digit number
                if 1000 <= perm_number <= 9999:
                    # Add the valid permutation to the list of permutations
                    permutations.append(perm_number)

# Find the minimum and maximum numbers from the permutations
min_number, max_number = min(permutations), max(permutations)

# Print the minimum and maximum possible numbers
print(min_number, max_number)
