# 📖 Story Continuation: The Tuple Team Assignments!

# With the student list restored, it's time to form teams for the competition! The Tech Club must use Tuples to assign students into teams, ensuring each team has exactly two members.

# 🔢 Python Tuple Challenges

# 1️⃣ Create a tuple named team_1 with the first two students from the student list.

# Your code here
studentList = ['Liam', ' Emma', ' Olivia', ' Noah', ' Sophia']     # from Assignment 3
team_1 = tuple(studentList[0:2])                                   # Extract two student from the list & stored into tuple
print(team_1)

# 2️⃣ Tuples are immutable! Try changing the second student's name in team_1 and note the error message.

# Your code here
#team_1[1] = "ABC"                           # Error : 'tuple' object does not support item assignment

# 3️⃣ Convert the team_1 tuple into a list, change the second student's name, and convert it back to a tuple.

# Your code here
team_1List = list(team_1)                       # convert it into list
team_1List[1] = "Amit"                           # update the list
team_1 = tuple(team_1List)                      # convert back into tuple
print(team_1)

# 4️⃣ Create a tuple named all_teams that contains three different teams, each as a tuple.

# Your code here
team_2 = ("Khushi", "Shantanu")
team_3 = ("Palak", "Suman")
all_teams = team_1 + team_2 + team_3
print(all_teams)
# 5️⃣ Use tuple unpacking to extract the student names from team_1 into separate variables and print them.

# Your code here
student1, student2 = team_1
print(student1)
print(student2)
# 🏆 Story Conclusion:
# With teams successfully assigned using tuples, the Tech Club is now fully prepared for the competition! But another challenge awaits—handling competition scores using dictionaries! 🚀
# 🎉 MISSION COMPLETE!
# Great job, Alex! You have successfully helped Greenfield High using Python! 🚀💡

