# 📌 TASK 3: Registering for the School Event (Input & Typecasting)
# 🔹 Scenario:

# The school is hosting a Chess Tournament, and students must be at least 12 years old to participate.
#
# 📝 Your Task:
#
# Ask the user to enter their age.
age = input("Enter your age : ")
# Convert the input to an integer.
age = int(age)
# Print if they are eligible or not.
if age >= 12:
    print("You are eligible")
else:
    print("Your are not eligible")


# ❌ Broken Code: ✅ Fix the below code using typecasting!

# #Fix the below code
# age = input("Enter your age: ")
# if age > 12:
#     print("You are eligible!")

age = input("Enter your age: ")
age = int(age)
if age > 12:
    print("You are eligible!")