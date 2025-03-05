# Dictionary are used to store data values in key:value pair (written with curly brackets) :
# A dictionary is a collection which is ordered(As of Python version 3.7), changeable and do not allow duplicates.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1994
}
print(thisdict)

# Access the specific item using key values :
print(thisdict["brand"])

# Duplicate values are not allowed in dictionary so it overwrite the previous values :
studentDic = {
    "enrol_no"  :   2100050062,
    "Name"  :   "Vivek Verma",
    "course"    :   "BCA",
    "enrol_no"  :   2220005610              # Overwrite the previous value.
}
print(studentDic)

print("The length of the studentDic dictionary is : ", len(studentDic))

# mix data type in dictionary

car = {
    "brand" :   "Ford",
    "Model" :   "Mustang",
    "electric"   :   False,
    "year"  :   1990,
    "Colors" :   ["Red", "Blue", "Black"]
}
print(car)

# data type :
print(type(car))

# Dict Constructor :
laptop = dict(compName = "Hewlett-packard", model = 2020, processor = "i3 10th gen")
print(laptop)

