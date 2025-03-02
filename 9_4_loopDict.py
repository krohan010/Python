# the looping through the dictionary, the return value are the key value of the dictionary :

studentData = {
    'id' : 120,
    'name' : 'Ankit Jha',
    'course' : "ADCA",
    'duration' : '3 years'
}

# for loop : default return key values only :
# for key in studentData:
#     print(key)

# Another way to print all keys :
# for key in studentData.keys():
#     print(key)

# print all values of dict :
# for key in studentData:
#     print(studentData[key])

# Another way to print all values of dict :
# for val in studentData.values():
#     print(val)

# Print both keys and values :
# for key in studentData:
#     print(key ," : ", studentData[key])

# Another way to print both key and value :
for key, val in studentData.items():
    print(key, val)