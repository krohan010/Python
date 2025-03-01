# 📌 TASK 11: Username Check (Special Operators - Identity)
# 🔹 Scenario:

# The school’s system needs to check if two usernames are the same.

# 📝 Your Task:

# Ask the user to enter their username twice.

# Use the identity operator (is) to check if they match.

# Print an appropriate message

# ***Solution***
username1 = str(input("Enter your username : "))
username2 = str(input("Re-enter your username : "))

# here "is" checks if the memory location of both variable are same or not
if username1 is username2:
    print("Both username are same")
else:
    print("The username differnt from other username")