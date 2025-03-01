# This section explains about how to add items in the list :

fruitList = ["Apple", "Banana", "Orange", "Pine-Apple"]

# At last...
fruitList.append("Strawberry")
print(fruitList)

# At specific location...
fruitList.insert(1, "Mango")         # Banana => Mango
print(fruitList)

# At Start
fruitList.insert(0, "Green Apple")
print(fruitList)

vegList = ["Tomato", "Potato"]

# combine and store two list
fruitList.extend(vegList)
print(fruitList)

# takes tuple value into list :
thisList = ["Apple", "Banana"]
thisTuple = ["Orange", "kiwi"]
thisList.extend(thisTuple)
print(thisList)
