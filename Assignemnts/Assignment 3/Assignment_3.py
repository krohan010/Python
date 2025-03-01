# 🏫 PYTHON SCHOOL QUEST: The Mystery of the Missing Student List!
# 🚀 A Fun, Beginner-Friendly Python Adventure! 🚀
# 📚 Chapter 3: Recovering the Lost Student List
# After automating the student enrollment system and handling calculations with operators, Principal Williams has another challenge for the Tech Club!
# 📝 The Challenge:
# The school's student attendance list for an upcoming coding competition has gone missing from the system. Without this list, the school won’t be able to register students for the event!
# The Tech Club (Alex, Mia, and Jake) must use Python Lists to recover, sort, modify, and manage the student list before the registration deadline.
# 🔢 Python List Challenges
# Part 1: Creating & Accessing Lists
# 1️⃣ The Tech Club finds a broken student list in the system:
from itertools import count

# students = "Liam, Emma, Olivia, Noah, Sophia"

# But this is a string, not a list! Convert it into a Python list and print it.

# #Write the code here
students = "Liam, Emma, Olivia, Noah, Sophia"
studentList = students.split(',')                       #string method (split()) splits the text into list
print(studentList)


# 2️⃣ The teacher finds out that "James" was also supposed to be on the list. Add "James" to the list.

# #Write the code here
studentList.append("James")                                 # add James at last

# 3️⃣ Alex wants to check who the first and last student is. Write a Python command to display both.

# #Write the code here
print(F"The first student is : {studentList[0]} \nAnd the last student is {studentList[len(studentList)-1]}")

# Part 2: Modifying Lists
# 4️⃣ Mia realizes there was a typo! "Olivia" should be "Olivia B." Modify the list to update the name.

# #Write the code here

# strip() method for removing space from beginning and end
for i in range(len(studentList)):
    studentList[i] = studentList[i].strip()

if "Olivia" in studentList:
# index() method search the name index number :
    studentList[studentList.index("Olivia")] = "Olivia B"
else:
    print("Olivia is not present in the list")

print(studentList)

# 5️⃣ Jake accidentally added "Noah" twice. Remove only one instance of "Noah" without deleting the whole list.

# #Write the code here

studentList.append("Noah")                      # accidentally added Noah twice
if studentList.count("Noah") == 2:              # checks that Two Noah is present in the list or not
    studentList.remove("Noah")                  # remove one Noah from the list
    print("One Noah is deleted")
else:                                           # Else condition
    print("Not deleted")
print(studentList)

# 6️⃣ Principal Williams says that "Ava" was missing from the list. Insert "Ava" at index 3 without replacing any existing students.

# #Write the code here
if "Ava" not in studentList:
    studentList.insert(3, "Ava")        # insert() method is used to add item at specific index
    print("Ava is added at 3 index")
else:
    print("Ava is already present in the list")
print(studentList)

# Part 3: Sorting & Reversing Lists
# 7️⃣ To make the list more organized, sort the student names alphabetically.

# #Write the code here

sortedStudentList = studentList.copy()                  # copy one list into new list
sortedStudentList.sort()                                # Alphabetically Ascending sort
print("Alphabetically sorted list is : ", sortedStudentList)

# 8️⃣ Mia suggests reversing the order of the list to check the last added names first. How can she do that?

#Write the code here
reverseStudentList = studentList.copy()                 # copy one list into new list
reverseStudentList.reverse()                            # Reverse the list
print("Last Added Display first order : ",reverseStudentList)

# Part 4: Slicing & Checking Elements
# 9️⃣ The competition only allows 4 students per school. Write a Python command to extract only the first 4 students from the list.

# #Write the code here
import random
competitorStudentList = studentList[0: 4]           # Extracting starting 4 students
print(competitorStudentList)

# 🔟 Jake wants to check if "Sophia" is on the list. Write a command that prints "Sophia is registered!" if she is found.

#Write the code here
if "Sophia" in studentList:                         # check whether sophia is present or not int the lis
    print("Sophia is Registered")
else:
    print("Not Registered!")

# Part 5: Advanced Operations
# 1️⃣1️⃣ The Tech Club finds an old list of students:

# old_students = ["Lucas", "Mia", "Henry"]

# Merge the old list with the new student list to make one combined list.

# #Write the code here
old_students = ["Lucas", "Mia", "Henry"]                    # old student list
studentList.extend(old_students)
print(studentList)

# 1️⃣2️⃣ The school needs at least 10 students for the competition. Use a loop to add placeholder students (e.g., "StudentX") until the list has 10 names.

# #Write the code here
# range(start, end, step) : start (included) end(not included)
for i in range(len(competitorStudentList), 10):
    competitorStudentList.append("StudentX")
print(competitorStudentList)

# 1️⃣3️⃣ Jake wants to check how many times "Emma" appears in the list. Write a command to count its occurrences.

# #Write the code here
print(F"Emma appears {studentList.count('Emma')} times in the list")

# 1️⃣4️⃣ Some names are mistakenly repeated. Write a command to remove duplicate names while keeping the original order.

studentList.insert(1, "Liam")
# #Write the code here
for i in range(len(studentList)):
    if studentList.count(studentList[i]) > 1:
        studentList[i] = ""

print(studentList)


# 1️⃣5️⃣ Principal Williams wants to start fresh. Write a Python command to clear all students from the list without deleting the variable.

# #Write the code here
studentList.clear()                 # Deleter all elements from the list