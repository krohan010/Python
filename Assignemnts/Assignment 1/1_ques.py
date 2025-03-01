# TASK 1: Student Enrollment System (Variables & Identifiers)
# 🔹 Scenario:

# Greenfield High is enrolling new students, and the system needs to store student information correctly.

# 📝 Mr. Carter’s Instructions:

# Create variables for a student’s name, student ID, and house color (Red, Blue, Green, or Yellow).

# Print the details in a friendly format.

# ✅ Example Output:
# Student Name: Emma
# Student ID: G2025
# House Color: Yellow

stu_name = "Emma"
stu_id = "G2025"
house_color = "Yellow"
print(F"The details are given below : \nStudent Name : {stu_name} \nStudent ID : {stu_id} \nHouse Color : {house_color}")


#  Fix This Code below (What’s Wrong?) 👉 Explain why these variable names are incorrect and rewrite them correctly.

# #Fix the below code
# 1name = "Emma"
# student-ID = "G2024"
# class = "Yellow"


# 1name = "Emma"                     # variable name must start with alphabet or underscore
name1 = "Emma"
# student-ID = "G2024"                # - symbol is not used in variable name
student_id = "G2024"
# class = "Yellow"                      # python keywords are not used as a variable name
house_color = "Yellow"

print(name1, student_id, house_color)