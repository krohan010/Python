# ASK 8: Even or Odd? (Arithmetic + Logical Operators)
# 🔹 Scenario:

# Alex wants to create a program that checks whether a number is even or odd.

# 📝 Your Task:

# Ask the user for a number.

# Use the modulus operator (%) to check if the number is even or odd.

# Print the result.

# ✅ Example Input & Output:

# Enter a number: 7

# 7 is an odd number!

rand_num = int(input("Enter any number : "))

is_even_no = rand_num%2
if(is_even_no==0):
    print(F"user input : {rand_num} is an Even Number.")
else:
    print(F"user input : {rand_num} is an Odd Number.")