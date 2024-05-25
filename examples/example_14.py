# Prompt the user to enter temperatures separated by spaces
input_temperatures = input("Enter temperatures separated by spaces: ")

# Split the input string into a list of individual temperature values
temperatures = list(map(int, input_temperatures.split()))

# Calculate the average temperature by summing all the temperatures and dividing by the number of temperatures
average_temperature = sum(temperatures) / len(temperatures)

# Count the number of days with temperatures not lower than the average
days_above_average = sum(1 for temp in temperatures if temp >= average_temperature)

# Print the number of days with temperatures not lower than the average
print(days_above_average)
