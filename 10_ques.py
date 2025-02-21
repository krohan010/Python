# 📌 TASK 10: The Discount Code (Special Operators - Membership)
# 🔹 Scenario:

# The Tech Club is offering a special discount code to selected students.

# 📝 Your Task:

# Check if the user’s name is in the discount list.

# Use the membership operator (in) to check eligibility.

# Print whether they get a discount.

# ✅ Example Names List:

# discount_students = ["Alex", "Mia", "Jake"]

# ***Solution***
import random
discount_students = ["Anuj", "Gaurav", "Kaif", "Rimjhim", "Payal", "Simran", "Preet"]
stu_name = input("Enter your Name : ")

if stu_name in discount_students:
    print(f"Your discount coupon  is : {random.randrange(10000,  99999)}")
else:
    print("You are not Eligible for discount coupon")