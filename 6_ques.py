# 📌 TASK 6: Logical Puzzle - School Entry (Logical Operators)
# 🔹 Scenario:

# To enter the Tech Lab, students must:

# Be at least 12 years old

# Have a Tech Club ID

# 📝 Your Task:

# Ask the user for their age and whether they have a Tech Club ID.

# Use logical operators (and, or, not) to check if they can enter.

# Print an appropriate message.

# ✅ Expected Output:

# Are you 12 years old or older? Yes

# Do you have a Tech Club ID? Yes

# Access Granted! Welcome to the Tech Lab!

# ***Solution****
age = int(input("Enter your age : "))
tech_id = input("Do you have tech id - say yes or no : ")

if age>=12 and tech_id == "yes":
    print("Are you 12 years old or older? " , bool(age>=12))
    print("Do you have a Tech Club ID? " , bool(tech_id=="yes"))
    print("Access Granted! Welcome to the Tech Lab!")
else:
    print("Access Rejected!")