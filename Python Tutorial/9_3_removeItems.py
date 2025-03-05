# There are several methods to remove items from the dictionary

studentData = dict({'id': 120, 'name': 'Ankit Jha', 'course': 'BCA', 'course_duration': '3 years'})

# 1. pop() : removes the item with the specified key name :
studentData.pop("course")                   # course item deleted
print(studentData)

# 2. popitem() : removes the last item
studentData.popitem()                       # last item deleted (course_duration : 3years)
print(studentData)

# 3. del keyword removes the item with the specified key name :
del studentData["id"]
print(studentData)

# 4. del keyword can also delete the dictionary. it means that dictionary will no more longer :
# del studentData
# print(studentData)                              # error occurred : studentData is not defined

# 5. clear() method empties the dictionary :
studentData.clear()
print(studentData)                                  # Display empty string