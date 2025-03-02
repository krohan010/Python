# Copy one dict to another dict :

studentData = {
    'id' : 120,
    'name' : 'Ankit Jha',
    'course' : "ADCA",
    'duration' : '3 years'
}
# 1. copy() method :
# copyStudentData = studentData.copy()
# print(copyStudentData)

# 2. dict() function :
copyStudentData = dict(studentData)
print(copyStudentData)


# Nested Dictionary : A dictionary can contain more than one dictionary :

# A dict contain three dict :
# employee = {
#     "emp1" : {
#         "name" : "Suman tiwari",
#         "YOJ" : 2022                        # YOJ : Year of Joining
#     },
# "emp2" : {
#         "name" : "Suraj Yadav",
#         "YOJ" : 2025
#     },
# "emp3" : {
#         "name" : "Akash singh",
#         "YOJ" : 2024
#     }
# }

# Another way to create Nested dictionary :
# Employee 1 :
emp1 = {
        "name" : "Suman tiwari",
        "YOJ" : 2022
    }
# Employee 2 :
emp2 = {
        "name" : "Suraj Yadav",
        "YOJ" : 2025
    }
# Employee 3 :
emp3 = {
        "name" : "Akash singh",
        "YOJ" : 2024
    }

# Combine them in one dict :
employee = {
    "emp1" : emp1,
    "emp2" : emp2,
    "emp3" : emp3
}

print(employee)
print(employee["emp1"])
print(employee["emp1"]["name"])

# empItem = employee.items()
# print(empItem)

for x, obj in employee.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
