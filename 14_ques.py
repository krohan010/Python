# TASK 14: Temperature Converter (Arithmetic Operators)
# 🔹 Scenario:

# Alex wants to convert Celsius to Fahrenheit using Python!

# 📝 Your Task:

# Ask the user to enter a temperature in Celsius.

# Use the formula:

# Fahrenheit = (Celsius * 9/5) + 32


# ***Solution***
celsius = int(input("Enter a temperature in celsius : "))
fahrenheit = float((celsius * 9/5) + 32)
print(F"The Fahrenheit value of {celsius} Celsius is : {fahrenheit}")