# Modify Items in the dictionary

studentData = {
    'id' : 120,
    'name' : 'Ankit Jha',
    'course' : "ADCA"
}

# change course name ADCA to BCA

# Using key :
# studentData["course"] = "BCA"

# Using update() method :
studentData.update({"course": "BCA"})
print(studentData)

# Add items int the studentData Dictionary :

# Add course_duration in studentData

# using key :
# studentData["course_duration"] = "3 Years"

# Using update() mehod
studentData.update({"course_duration": "3 years"})
print(studentData)