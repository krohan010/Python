# This section will teach you that how to join or combine two list :

fruitsList = ["Apple", "Strawberry", "Orange", "Mango"]
vegeList = ["Tomato", "Potato", "Cauliflower"]

# There are 3 ways to join two lists :

# First way :  using + operator
fruit_vege = fruitsList + vegeList
print(fruit_vege)

# Second way : Append method with loop
# for item in vegeList:
#     fruitsList.append(item)
# print(fruitsList)

# Third way : using extend method
fruitsList.extend(vegeList)
print(fruitsList)


