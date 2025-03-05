# this section explain about how to change data items

fruitList = ["Apple", "Banana", "Orange", "Kiwi", "WaterMelon"]
print(fruitList)

fruitList[0] = "Green-Apple"            # replace first element of list to "Green-Apple"
print(fruitList[0])

#removes 2 element  and add 2 element for a particular location of the list
fruitList[1:3] = ["Mango", "Strawberry"]
print(fruitList)

# remove 2 element and add 4 element for a particular location of the list
fruitList[3:5] = ["Bananas", "Orange", "Papaya", "Apricot"]
print(fruitList)

# You can also take negative values for indexing at the end...
