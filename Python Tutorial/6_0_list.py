# List are used to stored multiple items in a single variable
# List items are Ordered & Changeable and can be duplicate

fruitList = ["Apple", "Banana", "Orange"]

print(fruitList)

# List items are ordered, changeable, and can contain duplicate values
fruitList1 = ["Apple", "Banana", "Apple"]
print(fruitList1)

# Length of List :
print("The length of list is : ", len(fruitList))

# Datatype of list :
print(type(fruitList))

# A list can contain dissimilar type of data
anotherList = ["ABC", 25, "XYZ", 100]
print(anotherList)

# List Constructor :
# vegList = ["Tomato"]
vegList = list(("Tomato"))
print(vegList)                      # output : ['T', 'o', 'm', 'a', 't', 'o']