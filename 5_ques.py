# 📌 TASK 5: Scholarship Eligibility (Comparison Operators)
# 🔹 Scenario:

# To get a school scholarship, a student must have at least 90% in their final exam.

# 📝 Your Task:

# Ask the user to input their exam score.

# Use a comparison operator to check if they are eligible.

# Print an appropriate message.

# ***Solution***
score = int(input("Enter your marks in percentage(%) : "))
if score >= 90:
    print("Congratulation!, You are Eligible to get an scholarship")
else:
    print("Sorry!, You are not Elgible to get an scholarship")
