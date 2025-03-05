# This section describes that how to remove items from a list

fruitList = ["Apple", "Banana", "Orange", "Graphs", "Kiwi"]
print(fruitList)

# the remove() method removes the item from the list
# it removes first occurrence item
fruitList.remove("Graphs")
print(fruitList)

# The pop() method removes the last item
fruitList.pop()
print(fruitList)

# The pop() method also removes the specified index
fruitList.pop(1)
print(fruitList)

# The del keyword used to delete the list and its values.
# del fruitList                             # Delete the whole list
# print(fruitList)                          # throw an error because fruitList not exist
del fruitList[0]                            #deleter first (0) value from the list.
print(fruitList)

# The clear method removes the all elements into the list
# it still remains. but it has no contents
fruitList.clear()
print(fruitList)                                # returns empty list