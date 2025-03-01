# 📌 TASK 15: School Motto Formatting
# 🔹 Scenario:

# Print the school motto using a .format(), f-strings, and concatenation! Print the same motto with all the three methods

# Our motto: Welcome to Greenfield High! Our motto is Learn, Innovate, Succeed.

# Write the code here
welcomeMssg = "Welcome to Greenfield High!"
mottoKeyword = "Learn, Innovate, Succeed"

# F-string format
motto = (F"{welcomeMssg} Our motto is {mottoKeyword}")
print(motto)

# .format() method
print(motto.format())

# Normal String
print("Welcome to Greenfield High! Our motto is Learn, Innovate, Succeed.")