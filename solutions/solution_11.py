# Read the input
s = int(input())

# Calculate the number of bills for each denomination
bills_500 = s // 500
s %= 500

bills_100 = s // 100
s %= 100

bills_10 = s // 10
s %= 10

bills_5 = s // 5
s %= 5

bills_1 = s

# Print the number of bills for each denomination in one line
print(f"{bills_500} (500), {bills_100} (100), {bills_10} (10), {bills_5} (5), {bills_1} (1)")
