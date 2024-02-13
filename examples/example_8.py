# Read the input numbers from the user
a = int(input("Enter the cost of a book in pounds: "))
b = int(input("Enter the cost of a book in pennies: "))
n = int(input("Enter the number of books: "))

# Calculate the total cost in pennies
total_cost_in_pennies = (a * 100 + b) * n

# Calculate the number of pounds to be paid
pounds = total_cost_in_pennies // 100

# Calculate the number of pennies to be paid
pennies = total_cost_in_pennies % 100

# Print the number of pounds and pennies to be paid
print(pounds)
print(pennies)
