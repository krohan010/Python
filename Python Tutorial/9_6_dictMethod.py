# all methods of dict :

studentData = {
    'id' : 120,
    'name' : 'Ankit Jha',
    'course' : "ADCA",
    'duration' : '3 years'
}

# 1. clear() : removes all the elements from the dict :
# studentData.clear()
print(studentData)

# 2. copy() : return a copy of the dict :
copyStudentDat = studentData.copy()
print(copyStudentDat)

# 3. fromkeys() : returns a dictionary with the specified key and value :
keys = ("rollno", "name", "course", "duration")
values = 0
thisdict = dict.fromkeys(keys, values)
print(thisdict)                                 # return : {'rollno': 0, 'name': 0, 'course': 0, 'duration': 0}

# 4. get() : return the value of the specified key :
print(studentData.get("name"))

# 5. items() : Returns a list containing a tuple for each key value pair
print(studentData.items())

# 6. keys() : returns a list containing the directory's keys :
print(studentData.keys())

# 7. pop() : removes the element with the specified key :
studentData.pop('duration')
print(studentData)                              # no more exist 'duration' in the dictionary

# 8. popitem() : removes the last inserted key value pair :
studentData.popitem()
print(studentData)                              # course item deleted

# 9. setdefault() : Returns the value of the specified key. If the key does not exist: insert the key, with the specified values
studentData["duration"] = "3 Years"
studentData.setdefault("duration", "2 Years")       # if the value doesn't exist then only it prints.
print(studentData)

# 10. update() : Updates the dictionary with the specified key-value pairs
studentData.update({"teacher": "Rohan kumar"})
print(studentData)

# 11. values() : Returns a list of all the values in the dictionary
print(studentData.values())