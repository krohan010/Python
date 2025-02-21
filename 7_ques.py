# 📌 TASK 7: Robo-Helper’s Challenge (Logical Operators)
# 🔹 Scenario:

# Robo-Helper 3000 is only available for Tech Club members OR students who have completed their Python tasks.

# 📝 Your Task:

# Create two boolean variables: is_tech_club_member and completed_tasks.

# Use a logical operator to check if Robo-Helper can assist the student.

# Print the result

# ***Solution***
is_tech_club_member = bool(True)
completed_task = bool(True)
if is_tech_club_member and completed_task:
    print("Robo Helper can assist you!")
else:
    print("Robo Helper cannot assist you")