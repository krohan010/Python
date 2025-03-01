# 📌 TASK 2: Counting Students (Data Types & Typecasting)
# 🔹 Scenario:

# Principal Williams wants to know how many students are in school, but the system mistakenly stores the number as a string!

# 📝 Jake’s Question:

# "Hey Alex, why can’t I add 100 to total_students?"

# 📝 Your Task:

# Convert total_students from string to integer.
# Print the correct total number of students.

total_student = "100"
print("The value is :",total_student, type(total_student))
total_student = int(total_student)
print("The total number of student is :",total_student, type(total_student))

# ❌ Broken Code: ✅ Fix the below code using typecasting!

# #Fix the below code
# total_students = "500"
# print(total_students + 100)  #Error!

# The one operator (total_student) is string and another one is 100 is integer. we have convert convert sting into number.
total_students = "500"
total_students = int(total_students)
print(total_students + 100)